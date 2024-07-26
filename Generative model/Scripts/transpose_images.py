import os
from PIL import Image

base_path = "/home/shogg/RBHT projects/CVAE/Raw Input Images"

for subdir in os.listdir(base_path):
    subdir_path = os.path.join(base_path, subdir)
    if os.path.isdir(subdir_path):
        for filename in os.listdir(subdir_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(subdir_path, filename)
                with Image.open(file_path) as img:
                    mirrored = img.transpose(Image.FLIP_LEFT_RIGHT)
                    mirrored_filename = f"{os.path.splitext(filename)[0]}_mirrored{os.path.splitext(filename)[1]}"
                    mirrored.save(os.path.join(subdir_path, mirrored_filename))