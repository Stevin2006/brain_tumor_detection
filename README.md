# 🧠 Brain Tumor Detection using YOLOv8

A deep learning-based **MRI brain tumor classification system** built with YOLOv8 (classification mode) and deployed via a **Django web application**. Upload an MRI scan and get an instant AI-powered prediction.

---

## 📌 Project Overview

This project leverages the **Ultralytics YOLOv8 classification model** fine-tuned on brain MRI images to detect and classify brain tumors. A lightweight **Django web interface** allows users to upload MRI scans and receive predictions in real time.

---

## 🗂️ Project Structure

```
brain_tumor_detection/
│
├── Django/                        # Django web application
│   └── ...                        # Views, templates, URLs, settings
│
├── runs/
│   └── classify/
│       └── BrainTumorProject/
│           └── MRI_Classification_S/   # Training results & saved weights
│
├── training.py                    # Model training script
├── yolo26s-cls.pt                 # Pre-trained YOLOv8s-cls base weights
├── .gitignore
└── README.md
```

---

## 🧪 Model Training

The model was trained using the **YOLOv8 small classification variant** (`yolo26s-cls.pt`) on a labeled MRI dataset.

**Training Configuration:**

| Parameter | Value |
|-----------|-------|
| Model     | YOLOv8s-cls |
| Epochs    | 50 |
| Image Size | 224×224 |
| Batch Size | 16 |
| Project   | BrainTumorProject |

**Training Script (`training.py`):**

```python
from ultralytics import YOLO

model = YOLO("yolo26s-cls.pt")

model.train(
    data="Datasets",
    epochs=50,
    imgsz=224,
    batch=16,
    project="BrainTumorProject",
    name="MRI_Classification_S"
)
```

> The `Datasets/` folder should follow the standard YOLO classification structure with `train/` and `val/` subfolders, each containing class-named subdirectories.

---

## 📁 Dataset Structure (Expected)

```
Datasets/
├── train/
│   ├── glioma/
│   ├── meningioma/
│   ├── notumor/
│   └── pituitary/
└── val/
    ├── glioma/
    ├── meningioma/
    ├── notumor/
    └── pituitary/
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Stevin2006/brain_tumor_detection.git
cd brain_tumor_detection
```

### 2. Install Dependencies

```bash
pip install ultralytics django
```

### 3. Train the Model (Optional)

If you want to retrain from scratch:

```bash
python training.py
```

### 4. Run the Django Web App

```bash
cd Django
python manage.py runserver
```

Then open your browser at `http://127.0.0.1:8000/`

---

## 🌐 Web Application

The Django app provides a simple interface to:
- Upload an MRI scan image
- Run inference using the trained YOLO model
- Display the predicted tumor class with confidence

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Ultralytics YOLOv8 | Model training & inference |
| Django | Web framework |
| HTML/CSS | Frontend templates |

---

## 📊 Classes

The model classifies MRI scans into the following categories:

- **Glioma** — A tumor that starts in the glial cells of the brain
- **Meningioma** — A tumor arising from the meninges
- **Pituitary** — A tumor in the pituitary gland
- **No Tumor** — Healthy brain scan

---

## 👤 Author

**Stevin** — Computer Science Student  
GitHub: [@Stevin2006](https://github.com/Stevin2006)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> ⚠️ **Disclaimer:** This tool is built for educational purposes only and is **not** a substitute for professional medical diagnosis.
