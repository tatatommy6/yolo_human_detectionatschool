from ultralytics import YOLO
import cv2
model = YOLO("weights/best.pt")
img_path = "crowd.jpg"
result = model(img_path)
result = result[0]

boxes = result.boxes

img = cv2.imread(img_path)

for box in boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

cv2.imwrite("output.jpg",img)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()