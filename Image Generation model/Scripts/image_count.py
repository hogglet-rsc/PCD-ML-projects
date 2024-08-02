import os
from pathlib import Path

def count_images(directory):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    base_path = Path(directory)
    grand_total = 0

    for subfolder in base_path.iterdir():
        if subfolder.is_dir():
            count = sum(1 for file in subfolder.iterdir() if file.suffix.lower() in image_extensions)
            print(f"{subfolder.name}: {count} images")
            grand_total += count

    print(f"\nGrand total across all subdirectories: {grand_total} images")

count_images('/home/shogg/RBHT projects/CVAE/Raw Input Images')