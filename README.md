# PCD-ML-Models

This repository contains three machine learning models for diagnostics and research in Primary Ciliary Dyskinesia (PCD).

## Models

1. **Image Generation Model**
   - CVAE (Conditional Variational Autoencoder) for generating cilia cross sections.

2. **MTD Classification Model**
   - Detects, numbers and classifies microtubule doublets in ciliary images.
   - Works by drag and drop into graphical user interface.

3. **PCD Diagnostic Model**
   - XGBoost tree-based classifier.
   - Diagnoses PCD based on:
     - Genotype
     - Ciliary beat frequency
     - Electron Microscopy (EM) results
     - Immunofluorescence (IF) results
