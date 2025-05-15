#!/usr/bin/env python3
# split_data.py

import os
import random
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="images/labels 폴더에서 공통 파일명만 비율대로 나눠 train/val 리스트 생성")
    # 위치 인자에서 required 제거, --images 같은 옵션 인자로 변경
    parser.add_argument(
        "--images", "-i",
        required=True,
        help="원본 이미지 폴더 경로"
    )
    parser.add_argument(
        "--labels", "-l",
        required=True,
        help="원본 라벨(.txt) 폴더 경로"
    )
    parser.add_argument(
        "--train_file", "-t",
        required=True,
        help="생성할 train 리스트 파일명"
    )
    parser.add_argument(
        "--val_file", "-v",
        required=True,
        help="생성할 val 리스트 파일명"
    )
    parser.add_argument(
        "--ratio", "-r",
        type=float,
        default=0.8,
        help="train 비율 (0~1 사이, 기본 0.8)"
    )
    args = parser.parse_args()

    # 1. 이미지 폴더에서 사용 가능한 파일명(basename) 추출
    img_exts = {".jpg", ".jpeg", ".png", ".bmp"}
    imgs = [
        f for f in os.listdir(args.images)
        if os.path.splitext(f)[1].lower() in img_exts
    ]
    basenames = [os.path.splitext(f)[0] for f in imgs]

    # 2. 라벨 폴더에 .txt가 있는 파일명만 남기기
    valid = [
        b for b in basenames
        if os.path.isfile(os.path.join(args.labels, b + ".txt"))
    ]
    if not valid:
        print("❗ images와 labels 폴더에 공통된 파일명이 없습니다.")
        return

    # 3. 셔플 후 split
    random.shuffle(valid)
    split_idx = int(len(valid) * args.ratio)
    train_list = valid[:split_idx]
    val_list   = valid[split_idx:]

    # 4. train/val 리스트 파일에 기록
    with open(args.train_file, "w") as f:
        for name in train_list:
            f.write(name + "\n")
    with open(args.val_file, "w") as f:
        for name in val_list:
            f.write(name + "\n")

    print(f"[완료] 전체 {len(valid)}개 → train: {len(train_list)}, val: {len(val_list)}")
    print(f" • train 리스트 → {args.train_file}")
    print(f" • val 리스트   → {args.val_file}")

if __name__ == "__main__":
    main()
