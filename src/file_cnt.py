#데이터셋에 똥이 묻어있는지 확인하는 코드
import os

img_dir = '/Users/kimminkyeol/Programming/dataset/yolov8/output/train/images'
lbl_dir = '/Users/kimminkyeol/Programming/dataset/yolov8/output/train/labels'

img_files = set(os.path.splitext(f)[0] for f in os.listdir(img_dir) if f.endswith('.jpg'))
lbl_files = set(os.path.splitext(f)[0] for f in os.listdir(lbl_dir) if f.endswith('.txt'))

print("이미지 수:", len(img_files))
print("라벨 수:", len(lbl_files))
print("차이:", img_files.symmetric_difference(lbl_files))  # 이름이 안 맞는 것 확인
