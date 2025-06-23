# from ultralytics import YOLO
# import cv2
# import time

# model = YOLO("weights/best.pt")
# cap = cv2.VideoCapture(0) #실시간 영상 캡처를 위해 카메라 사용
# img_path = "crowd1.jpg"

# while True:
#     ret,frame = cap.read()
#     if not ret:
#         break

#     result = model(frame,conf=0.25, iou=0.5) #모델 정확도가 그리 높지 않아서 그래프를 보고 가장 최적의 파라미터를 찾음
#     boxes = result[0].boxes
#     cnt = 0

#     for box in result[0].boxes:
#         cls_id = int(box.cls[0].item())
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#         if cls_id == 8:
#             cnt += 1  # person이 아닌 경우 무시
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
#     print(f"Detected {cnt} people")

#     cv2.imshow("result", frame)
#     if cv2.waitKey(1)& 0xFF == ord('q'):
#         break
#     time.sleep(2)  # 0.1초 대기

# cap.release()
# cv2.destroyAllWindows()









#사진
from ultralytics import YOLO
import cv2
model = YOLO("weights/best.pt")
img_path = "img/crowd.jpg"
result = model(img_path,conf=0.25, iou=0.5) #모델 정확도가 그리 높지 않아서 그래프를 보고 가장 최적의 파라미터를 찾음
result = result[0]

boxes = result.boxes

img = cv2.imread(img_path)

cnt = 0

for box in boxes:
    cls_id = int(box.cls[0].item())
    if cls_id == 8:
        cnt += 1  # person이 아닌 경우 무시

    x1, y1, x2, y2 = map(int, box.xyxy[0])
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
print(f"Detected {cnt} people")

cv2.imwrite("img/crowd11.jpg",img)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()