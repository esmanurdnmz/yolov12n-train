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
```
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
```
---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/yolov12-object-detection.git
cd yolov12-object-detection
```

### 2. Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Install Ultralytics YOLOv12
```
pip install git+https://github.com/ultralytics/ultralytics.git
```


---


## 📊 Training the Model
To train the YOLOv12 model on the VOC dataset, run the following command:
```
python train.py
```
- **train.py** script handles the training process.

- **Make** sure the VOC dataset is correctly downloaded in the datasets/ folder.

- **You can** customize training parameters such as:
 
  - **Number** of epochs

  - **Batch** size

  - **Image** size

  - **Device** (CPU/GPU)

- **Training** results, logs, and trained weights are saved inside the runs/ directory by default.

---


## 🎥 Real-Time Video Inference

To run the trained YOLOv12 model on a sample video and visualize bounding boxes with center offset calculations, use:

```bash
python test_video.py
```

- **Detected** objects will be displayed with bounding boxes and center points.

- **X and Y** offsets (Δx, Δy) relative to the frame center will appear on the video.

- **The output** video is saved as output.mp4.

-Note: You can adjust the input video by replacing test.mp4 in the script.

---

## 🧪 Example Outputs
- **Detected objects:** Cars, motorbikes, persons (depending on dataset)

- **Sample output** includes center offset text overlay on each frame

- **Output video** demonstrates real-time inference capability

## ⚠️ Known Issues
- **Large .pt model** weights are not uploaded due to GitHub file size limits; download or train locally.

- **Batch size** and workers may need tuning depending on your hardware.

- **On Windows,** multiprocessing issues can be avoided by setting workers=0 in training.

## 📌 Conclusion
This project shows how YOLOv12 can be used for accurate and real-time object detection in videos.
Bounding box drawing, center offset calculation, and saving annotated video make it suitable for academic demos and experimental applications.
Further improvements are planned for model accuracy and deployment.

