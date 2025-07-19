import cv2
import torch
from ultralytics import YOLO


model = YOLO("runs/detect/train13/weights/best.pt")


video_path = "test.mp4"
cap = cv2.VideoCapture(video_path)


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter("output.mp4", fourcc, fps, (w, h))


frame_center = (w // 2, h // 2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break


    results = model(frame)[0]

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2


        offset_x = cx - frame_center[0]
        offset_y = cy - frame_center[1]


        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)


        text = f"X: {offset_x} px | Y: {offset_y} px"
        text_w, text_h = 260, 35
        margin = 10
        x_text = w - text_w - margin
        y_text = margin


        cv2.rectangle(frame, (x_text, y_text), (x_text + text_w, y_text + text_h), (50, 50, 50), -1)

        cv2.putText(frame, text, (x_text + 10, y_text + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    out.write(frame)


cap.release()
out.release()
cv2.destroyAllWindows()
