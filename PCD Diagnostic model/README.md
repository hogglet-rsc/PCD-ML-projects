# PCD Diagnostic Model

This XGBoost-based classifier diagnoses Primary Ciliary Dyskinesia (PCD) using multiple patient data points.

## Contents

- `detection_model.ipynb`: Main classification script

## Features

- Classifies patients as PCD or non-PCD
- Uses input data:
  - Electron microscopy results
  - Immunofluorescence results
  - Ciliary beat frequency
  - Genotype information

## Outputs

1. PCD classification for each patient
2. Precision-recall curve
3. Feature importance plot

## Usage

1. Prepare your dataset with required features
2. Run `detection_model.ipynb`
3. Review classification results and performance metrics

## Requirements

pip install requirements.txt
