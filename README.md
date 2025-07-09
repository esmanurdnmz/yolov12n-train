# YOLOv12-Based Real-Time Object Detection

This project demonstrates **object detection** using the YOLOv12 model.  
The model is trained on the VOC dataset and tested on a sample video with real-time bounding box drawing, center point marking, and X/Y offset calculations.
---

## 🚀 Project Overview

**Goal:** Train and test YOLOv12 on a custom dataset for general object detection.  
**Model Used:** YOLOv12n (Ultralytics)  
**Dataset:** VOC 2007/2012  
**Main Features:**
- Real-time object detection on video
- Bounding box drawing with center points
- Calculates X/Y offsets from frame center
- Displays offset values on the video overlay
- Saves final output as a video

---

## 📁 Project Structure

YOLOv12/
├── train.py # Script to train the model
├── test_video.py # Script to run detection on video
├── download_voc.py # Script to download VOC dataset
├── data/ # Data config files
├── datasets/ # Dataset folder (VOC)
├── models/ # Model weights and configs
├── runs/ # Training results (optional)
├── test.mp4 # Sample input video
├── output.mp4 # Example output video
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

# ⚙️ Installation

1. Clone the Repository:
```bash
git clone https://github.com/YOUR_USERNAME/yolov12-object-detection.git
cd yolov12-object-detection
2. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Install Ultralytics YOLOv12
pip install git+https://github.com/ultralytics/ultralytics.git

---
📊 Training the Model
Run training using the VOC dataset:
python train.py
Modify train.py to adjust epochs, batch size, image size, etc.

Training results are saved in the runs/ directory.

🎥 Run Object Detection
Run detection on a video file:
python test_video.py

Input video: test.mp4

Output video: output.mp4

Output includes bounding boxes, center points, and X/Y offset info.

📌 Notes
If your .pt weights are too large, use Git LFS.

For big datasets, it’s better to download them externally instead of uploading to the repo.

The project is still under development — model improvements and new features are planned.

