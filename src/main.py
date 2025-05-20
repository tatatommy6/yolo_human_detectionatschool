import cv2
from ultralytics import YOLO

model = YOLO("/Users/kimminkyeol/Programming/yolo_human_detectionatschool/yolov8n.pt")  
# img_path = ""
# img = cv2.imread(img_path)  

# results = model.predict(source= img, classes=[0])
# for result in results:
#     for box in result.boxes:
#         cls_id = int(box.cls[0])
#         if cls_id == 0:
#             x1,y1,x2,y2 = map(int, box.xyxy[0]) #box.xyxy[0] => 탐지된 객체의 좌상단 우상단 좌표
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
#             cv2.putText(img,"Person",(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),1)

# save_path = "../data/human_detected.jpg"
# cv2.imwrite(save_path, img) 
# print(f"Image saved at {save_path}")  
# cv2.imshow("Detected Image", img) 
# cv2.waitKey(0)  
# cv2.destroyAllWindows()  

#커스텀 데이터 학습할때 쓰는 코드
model.train(
    data = "dataset.yaml",  
    epochs = 10,  
    imgsz = 416,  
    batch = 12,  
    device = "mps",  
    name = "face_detector"
)
