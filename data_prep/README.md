# Data Preparation & PPE Dataset Pipeline (`/data_prep`)

This directory contains scripts and guidelines for downloading, preprocessing, and formatting Personal Protective Equipment (PPE) detection datasets required for training our lightweight YOLO model.

## 📦 Selected Public Datasets

We combine publicly available workplace safety datasets to ensure robust detection under varied industrial environments:

1. **Roboflow Worksite Safety / PPE Dataset:**
   - **Classes:** `person`, `hard-hat` (helmet), `safety-vest`, `no-helmet`, `no-vest`
   - **Format:** YOLOv8 / Roboflow Universe export format.
   - **Usage:** Primary dataset for training basic gear compliance.

2. **Pictor Construction Safety Dataset:**
   - **Focus:** Occluded workers, complex indoor/outdoor lighting, and distance variance in real factory settings.

## 🛠️ Data Pipeline Workflow

1. **Download:** Automated via `download_dataset.py` using Roboflow API.
2. **Preprocessing:** Frame resizing (640x640), normalization, and bounding-box validation.
3. **Export:** Converting annotations into standard ONNX-compatible format before running quantization through the **Hailo Dataflow Compiler**.
