# PCD-ML-Models

This repository contains three machine learning models for detection and research in Primary Ciliary Dyskinesia (PCD).

## Models

1. **Generative Model**
   - CVAE (Conditional Variational Autoencoder) for generating cilia cross sections

2. **Numbering Model**
   - Detects and numbers microtubule doublets in ciliary images

3. **PCD Diagnostic Model**
   - XGBoost tree-based classifier
   - Diagnoses PCD based on:
     - Genotype
     - Ciliary beat frequency
     - Electron Microscopy (EM) results
     - Immunofluorescence (IF) results