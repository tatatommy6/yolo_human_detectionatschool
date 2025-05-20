# import splitfolders

# splitfolders.ratio(
#     input="/Users/kimminkyeol/Programming/dataset/yolov8/com",
#     output="/Users/kimminkyeol/Programming/dataset/yolov8/output",
#     seed=42,
#     ratio=(0.8, 0.2),
#     group_prefix=1
# )


import os
import random
import shutil
from pathlib import Path

# 경로 설정
input_dir = Path("/Users/kimminkyeol/Programming/dataset/yolov8/com/cla")
output_dir = Path("/Users/kimminkyeol/Programming/dataset/yolov8/output")
train_ratio = 0.8

# 모든 이미지 파일 수집 (txt가 존재하는 것만)
image_files = [f for f in input_dir.glob("*.jpg") if (input_dir / (f.stem + ".txt")).exists()]
random.seed(42) #??????????
random.shuffle(image_files)

# 분할
split_idx = int(len(image_files) * train_ratio)
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

def copy_pairs(files, subset):
    img_out = output_dir / subset / "images"
    lbl_out = output_dir / subset / "labels"
    img_out.mkdir(parents=True, exist_ok=True)
    lbl_out.mkdir(parents=True, exist_ok=True)

    for img in files:
        lbl = input_dir / (img.stem + ".txt")
        shutil.copy2(img, img_out / img.name)
        shutil.copy2(lbl, lbl_out / lbl.name)

copy_pairs(train_files, "train")
copy_pairs(val_files, "val")

print("분할 완료")
