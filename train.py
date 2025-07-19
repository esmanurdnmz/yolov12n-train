from ultralytics import YOLO
import yaml

if __name__ == '__main__':

    with open('C:/Users/Esmanur/PycharmProjects/YOLOv12/datasets/VOC.yaml', encoding='utf-8') as f:
        voc_yaml = yaml.safe_load(f)


    model = YOLO('C:/Users/Esmanur/PycharmProjects/YOLOv12/models/yolo12n.pt')


    model.train(
        data='datasets/VOC.yaml',
        epochs=50,
        imgsz=640,
        batch=8,
        device=0,
        workers = 0
    )






















