from ultralytics import YOLO

# 1. Load the YOLO26s-cls model
model = YOLO("yolo26s-cls.pt")

# 2. Train the model
# For classification, just point 'data' to the root folder.
# YOLO will automatically look for 'train' and 'test'/'val' subfolders.
model.train(
    data="Datasets",
    epochs=50,
    imgsz=224,
    batch=16,
    project="BrainTumorProject",
    name="MRI_Classification_S"
)