#!/bin/bash

# Check if platipy is installed
if ! python3 -c "import platipy" &> /dev/null; then
    echo "Error: platipy package is not installed"
    echo "Please install platipy first using: pip install platipy"
    exit 1
fi

# Define the target directory
TARGET_DIR="$HOME/.local/lib/python3.8/site-packages/platipy/imaging/utils"

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Directory $TARGET_DIR does not exist"
    exit 1
fi

# Check if lung.py exists in the target directory
if [ -f "$TARGET_DIR/lung.py" ]; then
    echo "Backing up existing lung.py to lung-org.py"
    mv "$TARGET_DIR/lung.py" "$TARGET_DIR/lung-org.py"
fi

# Copy the local lung.py to the target directory
if [ -f "lung.py" ]; then
    echo "Copying new lung.py to $TARGET_DIR"
    cp "lung.py" "$TARGET_DIR/"
    echo "Installation completed successfully"
else
    echo "Error: lung.py not found in current directory"
    exit 1
fi
