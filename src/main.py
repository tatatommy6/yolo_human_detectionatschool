import cv2
from ultralytics import YOLO

model = YOLO("/Users/kimminkyeol/Programming/yolo_human_detectionatschool/yolov8n.pt")  # Load a pretrained YOLOv8 model
# img_path = "/Users/kimminkyeol/Programming/yolo_human_detectionatschool/data/human1.jpg"
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
# cv2.imwrite(save_path, img)  # Save the image with detected objects
# print(f"Image saved at {save_path}")  # Print the save path
# cv2.imshow("Detected Image", img)  # Display the image with detected objects
# cv2.waitKey(0)  # Wait for a key press to close the image window
# cv2.destroyAllWindows()  # Close all OpenCV windows
train_imgs= ""
val_imgs = ""
train_labels = ""
val_labels = ""

data_dict = {
    'train': train_imgs,
    'val': val_imgs,
    'nc': 1,  
    'names': {0,'face'} 
}

model.train(
    data = "dataset.yaml",  # Path to the dataset YAML file
    epochs = 10,  # Number of training epochs
    imgsz = 416,  # Image size for training
    batch = 12,  # Batch size for training
    device = "mps",  # Device to use for training (0 for GPU, 'cpu' for CPU)
    name = "face_detector"
)
