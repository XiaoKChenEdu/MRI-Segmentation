# MRI Segmentation Tool

An MRI segmentation tool for lung and heart segmentation using PlatyPy library.

## Environment

- Ubuntu 20.04
- Python 3.8.10

## Installation

1. Clone this repository:
```bash
git clone https://github.com/XiaoKChenEdu/MRI-Segmentation
cd MRI-Segmentation
```

2. Install uv (if not already installed):
```bash
pip install uv
```

3. Install dependencies using uv:
```bash
uv install .
source .venv/bin/activate
pip install platipy[cardiac]
```

4. Install the custom lung segmentation module:
```bash
chmod +x install_lung.sh
./install_lung.sh
```

## Dependencies

This project uses `uv`, a fast Python package installer and resolver. Learn more about uv at [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv).

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