import os
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import MRIUploadForm
from .models import MRIScan
from ultralytics import YOLO

# 1. Load the model globally so it doesn't reload on every click (saves memory/time)
# Ensure this path matches where your training finished
MODEL_PATH = os.path.join(settings.BASE_DIR,  'model1.pt')

# Load the model once
try:
    model = YOLO(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


def upload_mri(request):
    scan_obj = None

    if request.method == 'POST':
        form = MRIUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form but don't commit to DB yet so we can add prediction data
            scan_obj = form.save(commit=False)
            scan_obj.save()  # Save to get the file path on disk

            if model:
                # 2. Run YOLO26s-cls Inference
                # Use scan_obj.image.path to get the absolute system path
                results = model.predict(scan_obj.image.path)

                for r in results:
                    # Get the top class name (e.g., 'glioma')
                    top_label = r.names[r.probs.top1]
                    # Get the confidence score as a percentage
                    conf_score = round(float(r.probs.top1conf) * 100, 2)

                    # 3. Update the object with AI results
                    scan_obj.prediction = top_label
                    scan_obj.confidence = conf_score
                    scan_obj.save()
            else:
                scan_obj.prediction = "Error: Model not loaded"
                scan_obj.save()

    else:
        form = MRIUploadForm()

    # Get recent history to show on the page (optional)
    history = MRIScan.objects.all().order_by('-uploaded_at')[:5]

    return render(request, 'upload.html', {
        'form': form,
        'scan_obj': scan_obj,
        'history': history
    })