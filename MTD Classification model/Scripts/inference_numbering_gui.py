# import modules 
from geti_sdk.deployment import Deployment
import cv2
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import transforms
import numpy as np
from pprint import pprint
import math
import copy
import json
import os
import csv
import pandas as pd

# load inference models
numbering_model_path = "../Deployed models/Numbering/deployment"
classification_model_path = "../Deployed models/Classification/deployment"
numbering_deployment = Deployment.from_folder(numbering_model_path)
numbering_deployment.load_inference_models(device="CPU")

# when classification model is downloaded, place in 'Deployed models/Classification' 
# folder and uncomment the next two lines to deploy
# classification_deployment = Deployment.from_folder(classification_model_path)
# classification_deployment.load_inference_models(device="CPU")

def plot_rotated_rectangle(ax, x, y, width, height, angle, color, label=None):
    rect = Rectangle((x - width/2, y - height/2), width, height,
                     fill=False, edgecolor=color, linewidth=2)
    t = plt.gca().transData
    rotation = transforms.Affine2D().rotate_deg_around(x, y, angle)
    t = rotation + t
    rect.set_transform(t)
    ax.add_patch(rect)
    if label:
        ax.text(x, y, label, color='white', fontweight='bold', ha='center', va='center')

def draw_perpendicular_line(ax, x, y, width, height, angle, image_shape):
    img_height, img_width = image_shape[:2]
    
    # Ensure angle is perpendicular to long axis
    if width > height:
        angle += 90
    
    # Convert angle to radians
    angle_rad = math.radians(angle)
    
    # Calculate the line's slope
    slope = math.tan(angle_rad)
    
    # Calculate the line's intercept
    intercept = y - slope * x
    
    # Find intersections with image boundaries
    if abs(slope) > 1e-6:  # Non-vertical line
        x1 = 0
        y1 = intercept
        x2 = img_width
        y2 = slope * img_width + intercept
        
        # Check if line intersects top or bottom
        if y1 < 0:
            y1 = 0
            x1 = -intercept / slope
        elif y1 > img_height:
            y1 = img_height
            x1 = (img_height - intercept) / slope
        
        if y2 < 0:
            y2 = 0
            x2 = -intercept / slope
        elif y2 > img_height:
            y2 = img_height
            x2 = (img_height - intercept) / slope
    else:  # Vertical line
        x1 = x2 = x
        y1 = 0
        y2 = img_height
    
    # Draw the line
    ax.plot([x1, x2], [y1, y2], color='red', linewidth=2)
    return ((x1, y1), (x2, y2))

def distance_to_line(point, line_start, line_end):
    x, y = point
    x1, y1 = line_start
    x2, y2 = line_end
    return abs((y2-y1)*x - (x2-x1)*y + x2*y1 - y2*x1) / math.sqrt((y2-y1)**2 + (x2-x1)**2)

def distance_between_points(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def number_mtd_boxes(mtd_boxes, bmt_boxes, line_start, line_end):
    mtd1 = min(mtd_boxes, key=lambda box: distance_to_line((box['x'], box['y']), line_start, line_end))
    mtd1['number'] = 1
    bmt1 = min(bmt_boxes, key=lambda box: distance_between_points((box['x'], box['y']), (mtd1['x'], mtd1['y'])))
    
    numbered_mtds = [mtd1]
    unnumbered_mtds = [box for box in mtd_boxes if box != mtd1]
    
    for i in range(2, 10):
        if i == 2:
            distances = sorted([(box, distance_between_points((box['x'], box['y']), (bmt1['x'], bmt1['y']))) for box in unnumbered_mtds], key=lambda x: x[1])
            next_mtd = distances[1][0]
        else:
            prev_mtd = numbered_mtds[-1]
            next_mtd = min(unnumbered_mtds, key=lambda box: distance_between_points((box['x'], box['y']), (prev_mtd['x'], prev_mtd['y'])))
        
        next_mtd['number'] = i
        numbered_mtds.append(next_mtd)
        unnumbered_mtds.remove(next_mtd)
    
    return {(box['x'], box['y']): box['number'] for box in numbered_mtds}

def process_image(image_path, prediction_dict, output_folder, unusable_folder):
    # Load and process image
    dummy_image = cv2.imread(image_path)
    dummy_image = cv2.cvtColor(dummy_image, cv2.COLOR_BGR2RGB)

    # Create figure and axes
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(dummy_image)
    ax.invert_yaxis()

    # Separate boxes by type
    mtd_boxes, bmt_boxes, cp_box = [], [], None
    for annotation in prediction_dict['annotations']:
        shape = annotation['shape']
        name = annotation['labels'][0]['name']
        box = {k: shape[k] for k in ['x', 'y', 'width', 'height', 'angle']}
        box['color'] = annotation['labels'][0]['color']
        
        if name == 'MTD':
            mtd_boxes.append(box)
        elif name == 'B-MT':
            bmt_boxes.append(box)
        elif name == 'CP':
            cp_box = box

    # Check if image is usable (has CP and exactly 9 MTDs)
    is_usable = cp_box is not None and len(mtd_boxes) == 9

    # Plot all boxes (MTD, B-MT, and CP)
    for annotation in prediction_dict['annotations']:
        shape = annotation['shape']
        name = annotation['labels'][0]['name']
        color = annotation['labels'][0]['color']
        label = name if name == 'CP' else None
        plot_rotated_rectangle(ax, shape['x'], shape['y'], shape['width'], shape['height'], shape['angle'], color, label)

    if is_usable:
        line_points = draw_perpendicular_line(ax, cp_box['x'], cp_box['y'], cp_box['width'], cp_box['height'], cp_box['angle'], dummy_image.shape)
        numbered_mtds = number_mtd_boxes(mtd_boxes, bmt_boxes, line_points[0], line_points[1])

        # Add numbers to MTD boxes
        for box in mtd_boxes:
            mtd_number = numbered_mtds.get((box['x'], box['y']), np.nan)
            ax.text(box['x'], box['y'], f"MTD{mtd_number}", color='white', fontweight='bold', ha='center', va='center')

    # Adjust plot to remove extra whitespace
    ax.set_xlim(0, dummy_image.shape[1])
    ax.set_ylim(dummy_image.shape[0], 0)  # Reverse y-axis to match image coordinates
    plt.axis('off')
    plt.tight_layout()
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)
    
    # Save the image
    image_filename = os.path.basename(image_path)
    if is_usable:
        save_folder = output_folder
        prefix = 'numbered_'
    else:
        save_folder = output_folder
        prefix = 'unusable_'
    
    save_path = os.path.join(save_folder, f'{prefix}{image_filename}')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close()

    # Create an empty DataFrame outside the if statement
    df = pd.DataFrame(columns=['MTD_number', 'origin_x', 'origin_y'])

    if is_usable:
    # Create DataFrame for MTD coordinates
        df_data = []
        for i in range(1, 10):
            mtd = next((box for box in mtd_boxes if numbered_mtds.get((box['x'], box['y'])) == i), None)
            if mtd:
                df_data.append([i, mtd['x'], mtd['y']])
            else:
                df_data.append([i, '', ''])
        
        df_filename = f'MTD_coords_{os.path.splitext(image_filename)[0]}'
        df = pd.DataFrame(df_data, columns=['MTD_number', 'origin_x', 'origin_y'])
    
    # You can return the DataFrame or store it as needed
    return is_usable, df

# Main processing loop
input_folder = '../Images/GUI/Raw Images GUI'
output_folder = '../Images/GUI/Processed Images GUI' 

# Ensure the output and unusable folders exist
os.makedirs(output_folder, exist_ok=True)

for image_file in os.listdir(input_folder):
    if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_folder, image_file)
        
        try:
            # Generate numbering
            input_image = cv2.imread(image_path)
            numbering_prediction = numbering_deployment.infer(input_image)
            numbering_prediction_dict = numbering_prediction.to_dict()
            is_usable, MTD_coords_df = process_image(image_path, numbering_prediction_dict, output_folder, output_folder)
            
            # Generate MTD labels
            # MTD_classification_dict = classification_deployment.infer(input_image).to_dict()

            status = "usable" if is_usable else "unusable"
            print(f"Processed {image_file} - {status}")
        
        except Exception as e:
            print(f"Error processing {image_file}: {str(e)}")
            continue

print("All images processed.")