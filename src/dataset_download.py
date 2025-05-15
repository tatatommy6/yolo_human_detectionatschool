import kagglehub

# Download latest version
path = kagglehub.dataset_download("lylmsc/wider-face-for-yolo-training")

print("Path to dataset files:", path)