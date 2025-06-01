import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")  

#커스텀 데이터 학습할때 쓰는 코드
model.train(
    data = "dataset.yaml",  
    epochs = 10,  
    imgsz =  640,  
    device = "mps",  
    name = "crowd_detector"
)