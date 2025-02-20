# MRI Segmentation Project

This repository contains tools for automated segmentation of lung and heart structures from medical imaging data using the PlatIPy framework.

## Overview

The project provides automated segmentation capabilities for:
- Lung segmentation
- Heart segmentation

## Prerequisites

- Python 3.8
- SimpleITK
- PlatIPy framework
- Matplotlib

## Installation

1. Install the required Python packages:
```bash
pip install platipy SimpleITK matplotlib
```

2. Install the custom lung segmentation module:
```bash
chmod +x install_lung.sh
./install_lung.sh
```

## Directory Structure

```
.
├── input/
│   └── volumes/          # Place your .nii.gz volume files here
├── output/               # Segmentation results will be saved here
├── lung.py               # Lung segmentation utility functions
├── lung_segmentation.py  # Lung segmentation script
├── heart_segmentation.py # Heart segmentation script
└── install_lung.sh       # Installation script for lung module
```

## Usage

1. Place your medical volume files (in .nii.gz format) in the `input/volumes/` directory.

2. For lung segmentation:
   ```bash
   python3 lung_segmentation.py
   ```

3. For heart segmentation:
   ```bash
   python3 heart_segmentation.py
   ```

4. Results will be saved in the `output/` directory with the following structure:
   ```
   output/
   └── volume_X/
       ├── volume_X_Auto_Lung.nii.gz
       ├── volume_X_lung_visualization.png
       ├── volume_X_Heart.nii.gz
       └── volume_X_heart_visualization.png
   ```

## File Descriptions

- `lung.py`: Contains utility functions for hole detection and lung mask generation
- `lung_segmentation.py`: Main script for lung segmentation using PlatIPy
- `heart_segmentation.py`: Main script for heart segmentation using PlatIPy's hybrid segmentation
- `install_lung.sh`: Installation script for the lung module

## Note

Make sure to modify the `filename` variable in both segmentation scripts to match your input volume filename.
