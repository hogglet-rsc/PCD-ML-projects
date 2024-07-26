# CVAE for Cilia Cross Section Image Generation

## Overview

This project uses a Conditional Variational Autoencoder (CVAE) to generate synthetic images of cilia cross sections. The primary goal is to supplement the training data for detection models used in Primary Ciliary Dyskinesia (PCD) research and diagnostics.


## Dataset

The dataset consists of anonymized labelled cilia cross sections:

- Total images: 5,210
- Training split: 80% (4,168 images)
- Testing split: 20% (1,042 images)
- Classes: Normal, Disarranged, Outer dynein arm defects, Inner dynein arm defects, central pair defects

## Directory Structure

- **Best Models & Tensors**: Saved results of previous large training runs
- **Current Models & Tensors**: Outputs of most recent training run
- **Generated Images 224x224**: Generated images at 224x224 resolution
- **Generated Images 448x448**: Generated images at 448x448 resolution
- **Image Comparison**: Compares examples from training set and generated images of each resolution
- **Processed Input Images**: Preprocessed dataset for CVAE training
- **Raw Input Images**: Original, anonymized cilia cross section images
- **Scripts**: Main Python scripts for preprocessing, training, and inference

## Main Scripts

1. **cvae_pre_processing.py**: Prepares raw images for CVAE input
2. **cvae_training_224x224.py**: Trains the 224x224 CVAE model
3. **cvae_training_448x448.py**: Trains a larger 448x448 CVAE model (requires more compute)
4. **cvae_inference.py**: Generates synthetic examples using trained models

## Usage

1. **Environment Setup**:
   - Clone the repository:
     ```
     git clone https://github.com/yourusername/CVAE-Cilia-Generation.git
     cd CVAE-Cilia-Generation
     ```
   - Set up a virtual environment (optional but recommended):
     ```
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```
   - Install required packages:
     ```
     pip install -r requirements.txt
     ```

2. **Data Preparation**:
   - Place your raw cilia cross section images in the `Raw Input Images` folder.
   - Organize images by class in separate subfolders (e.g., Normal, Disarranged).
   - Ensure images follow the naming convention: `[Class]_[Number]` (e.g., Normal_0001).

3. **Preprocessing**:
   - Run the preprocessing script, specifying desired resolution at top of script:
     ```
     python Scripts/cvae_pre_processing.py
     ```
   - This will process the raw images and save the results in `Processed Input Images`.
   - Check `raw_image_statistics.csv` in the same folder for dataset statistics.

4. **Model Training**:
   - Start the training process:
     ```
     python Scripts/cvae_training.py
     ```
   - The script will use the preprocessed images to train the CVAE model.
   - Trained encoder and decoder models will be saved in the `Models` directory.
   - Latent space tensors will be stored in `Latent Space Tensors`.

5. **Generating Synthetic Images**:
   - Run the inference script:
     ```
     python Scripts/cvae_inference.py
     ```
   - This will use the trained decoder model and latent space tensors to generate synthetic images.
   - Generated images will be saved in the `Generated Images` folder.


## Further Work

Several avenues for potential improvement:

1. **Larger Labelled Dataset**: 
   - Expanding the training dataset could significantly enhance the model's ability to capture the full range of cilia variations.
   - A larger dataset would likely lead to more diverse and accurate synthetic image generation.

2. **Higher Resolution Images**: 
   - The current model generates images at 224x224 pixels, while the average input dimension is 524x508.
   - Increasing the output resolution to match or exceed the average input size could preserve more detail.

3. **Adaptive Input Size**: 
   - The current preprocessing step compresses all images to a square format, potentially losing aspect ratio information.
   - Implementing an adaptive input size could better preserve the original image proportions and structural details.

4. **Model Scaling**:
   - Increasing the number of parameters in the model could potentially capture more complex patterns in the data.
   - Utilizing more computational resources for training (e.g., longer training times, distributed training) might yield performance improvements.

5. **Advanced Architectures**:
   - Exploring more recent architectures e.g. cGAN, Transformer or Diffusion-based architectures, could improve performance.

## Requirements

- Python 3.7+
- TensorFlow 2.x
- NumPy
- Matplotlib
- Pandas

For a complete list of dependencies, see `requirements.txt`.

## Contributing

We welcome contributions to improve the model's performance or extend its capabilities. Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the (LICENSE) file for details.

## Acknowledgments

- Thanks to Royal Brompton hospital for providing the cilia cross section dataset.
- This project builds upon the work of Mersico at https://www.kaggle.com/code/mersico/cvae-from-scratch.

## Contact

For any queries regarding this project, please contact Struan Hogg at sjmhogg@gmail.com.