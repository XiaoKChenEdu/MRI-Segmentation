# MRI Segmentation Tool

An MRI segmentation tool for lung and heart segmentation using PlatyPy library.

## Environment

- Ubuntu 20.04
- Python 3.8.10

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/MRI-Segmentation.git
cd MRI-Segmentation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install the custom lung segmentation module:
```bash
chmod +x install_lung.sh
./install_lung.sh
```

## Dependencies

The following Python packages are required:

- platipy==0.5.1
- SimpleITK==2.2.1
- matplotlib==3.7.1
- numpy==1.24.3

## Project Structure

```
MRI-Segmentation/
├── requirements.txt
├── lung_segmentation.py
├── lung_segmentation_gui.py
├── heart_segmentation.py
├── heart_segmentation_gui.py
├── input/
│   └── volumes/
└── output/
```

## Usage

### GUI Tools

1. For lung segmentation:
```bash
python lung_segmentation_gui.py
```

2. For heart segmentation:
```bash
python heart_segmentation_gui.py
```

### Command Line Tools

1. For lung segmentation:
```bash
python lung_segmentation.py
```

2. For heart segmentation:
```bash
python heart_segmentation.py
```

## Input Format

The tool accepts NIFTI files (*.nii.gz) as input. Place your input files in the `input/volumes/` directory.

## Output

The segmentation results will be saved in the `output/` directory, organized in subdirectories named after the input file. Each output directory contains:
- Segmentation masks in NIFTI format (*.nii.gz)
- Visualization of the segmentation (PNG format)