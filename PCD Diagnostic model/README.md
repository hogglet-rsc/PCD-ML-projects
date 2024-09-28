# PCD Diagnostic Model

This XGBoost classifier diagnoses Primary Ciliary Dyskinesia (PCD) based on 4 diagnostic tests.

## Contents

- `diagnostic_model.ipynb`: Main classification script

## Features

- Classifies patients as PCD or non-PCD
- Uses input data:
  - Electron microscopy results
  - Immunofluorescence results
  - Ciliary beat frequency
  - Genotype information

## Outputs

1. PCD classification (Y/N) for each patient.
2. Precision-recall curve (demonstrates performance across a range of classification thresholds).
3. Feature importance plot (can be used to compare historical weighting of different diagnostic techniques).

## Environment Setup

   - Clone the repository:
     ```
     git clone https://github.com/hogglet-rsc/PCD-ML-projects.git
     cd 'PCD Diagnostic model'
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

## Usage

1. Compile your dataset with required features
2. Run `detection_model.ipynb`

