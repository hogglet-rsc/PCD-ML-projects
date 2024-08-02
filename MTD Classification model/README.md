# Microtubule Doublet Numbering Model

This model detects, numbers and classifies microtubule doublets (MTDs) in ciliary cross-section images.

## Usage

1. **Environment Setup**:
   - Clone the repository:
     ```
     git clone https://github.com/hogglet-rsc/PCD-ML-projects.git
     cd 'MTD Classification model'
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

2. Run `gui.ipynb` if working via gui.
3. If not working via gui, copy images into 'Images/Raw Images' folder.
2. Run `inference_numbering.ipynb`
3. Processed Images are saved in 'Images/Processed Images', with summary statistics saved in 'Summary data/mtd_analysis.xlsx'

Note: Images require 9 MTDs and 1 CP for successful numbering, otherwise 'Unusable'
