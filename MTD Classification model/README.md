# Microtubule Doublet Numbering Model

This model detects and numbers microtubule doublets (MTDs) in ciliary cross-section images.

## Components

- Intel GETi classification model (in `deployment` folder)
- `inference_numbering.ipynb` for processing images

## Features

- Detects MTDs, B-microtubules (MTD-B), and central pair (CP)
- Numbers MTDs based on spatial orientation
- Processes images from 'Raw Images' folder
- Saves numbered images in 'Numbered Images' folder
- Saves unusable images in 'Unusable Images' folder
- Plots detection boxes on all processed images
- Saves x-y coordinates and numbers (1-9) for each MTD

## Usage

1. Place raw images in 'Raw Images' folder
2. Run `inference_numbering.ipynb`
3. Check results in respective output folders


Note: Images require 9 MTDs and 1 CP for successful numbering, otherwise 'Unusable'