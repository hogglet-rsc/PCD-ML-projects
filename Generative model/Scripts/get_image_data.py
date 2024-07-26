import os
from PIL import Image
import numpy as np
from collections import Counter

def get_image_info(directory):
    image_sizes = []
    color_modes = []
    bit_depths = []
    max_pixels = []
    aspect_ratios = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        image_sizes.append((width, height))
                        color_modes.append(img.mode)
                        img_array = np.array(img)
                        if img_array.dtype == np.uint8:
                            bit_depths.append(8)
                        elif img_array.dtype == np.uint16:
                            bit_depths.append(16)
                        else:
                            bit_depths.append(f"Unknown ({img_array.dtype})")
                        max_pixels.append(np.max(img_array))
                        aspect_ratios.append(width / height)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    if not image_sizes:
        return "No image files found."

    widths, heights = zip(*image_sizes)

    size_counts = Counter(image_sizes)
    mode_counts = Counter(color_modes)
    depth_counts = Counter(bit_depths)

    return f"""
Total images processed: {len(image_sizes)}

Width:
  Max: {max(widths)}
  Min: {min(widths)}
  Avg: {sum(widths) / len(widths):.2f}

Height:
  Max: {max(heights)}
  Min: {min(heights)}
  Avg: {sum(heights) / len(heights):.2f}

Aspect Ratio:
  Max: {max(aspect_ratios):.2f}
  Min: {min(aspect_ratios):.2f}
  Avg: {sum(aspect_ratios) / len(aspect_ratios):.2f}

# Image dimensions:
# {', '.join(f'{w}x{h}: {count}' for (w, h), count in size_counts.most_common(10))}
# {f'... and {len(size_counts) - 10} more' if len(size_counts) > 10 else ''}

# Color modes:
# {', '.join(f'{mode}: {count}' for mode, count in mode_counts.items())}

# Bit depths:
# {', '.join(f'{depth}-bit: {count}' for depth, count in depth_counts.items())}

Max pixel value range: {min(max_pixels)} to {max(max_pixels)}
"""

# Usage
directory = '/home/shogg/RBHT projects/CVAE/Raw Input Images/CVAE_train'
print(get_image_info(directory))