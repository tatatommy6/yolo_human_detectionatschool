#split-folders 쓰고싶은데 ㅜㅜㅜㅜㅜㅜ

# import splitfolders

# splitfolders.ratio(
#     input="/Users/kimminkyeol/Programming/dataset/yolov8/com",
#     output="/Users/kimminkyeol/Programming/dataset/yolov8/output",
#     seed=42,
#     ratio=(0.8, 0.2),
#     group_prefix=1
# )
import random
import shutil
from pathlib import Path
# 경로 설정
input_dir = Path("/Users/kimminkyeol/Programming/dataset/yolov8/com/cla")
output_dir = Path("/Users/kimminkyeol/Programming/dataset/yolov8/output")
train_ratio = 0.8

# 모든 이미지 파일 수집 (txt가 존재하는 것만)
image_files = [f for f in input_dir.glob("*.jpg") if (input_dir / (f.stem + ".txt")).exists()]

'''glob 함수는 사용자가 제시한 조건에 맞는 파일명을 리스트 형식으로 반환한다고함.
stem은 확장자를 제외한 파일 이름을 반환하는 메서드임.
image_files에는 이미지 파일의 경로만 들어감 .txt파일들은 존재여부만 확인함.
.txt파일이 있어야지 .jpg파일이 image_files에 들어감'''

random.seed(42) #규칙같음 42쓰는건 
random.shuffle(image_files) #파일 순서를 무작위로 바꿔줌

# 분할
split_idx = int(len(image_files) * train_ratio) # 0.8을 곱함

#곱한 수를 기준으로 슬라이싱
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
