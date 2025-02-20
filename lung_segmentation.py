#!/usr/bin/python3

import os

import platipy

import SimpleITK as sitk
import matplotlib.pyplot as plt

from platipy.imaging.projects.bronchus.run import run_bronchus_segmentation
from platipy.imaging import ImageVisualiser
from platipy.imaging.label.utils import get_com

### Change this ###
filename = f'volume_{90}'
### Change this ###

os.makedirs(f"./output/{filename}", exist_ok=True)
test_image = sitk.ReadImage(f"./input/volumes/{filename}.nii.gz")
auto_structures = run_bronchus_segmentation(test_image)

output_directory = './output'

for struct_name in list(auto_structures.keys()):
    sitk.WriteImage(auto_structures[struct_name], str(f"{output_directory}/{filename}/{filename}_{struct_name}.nii.gz"))

print(f"Segmentations saved to: {output_directory}")

vis = ImageVisualiser(test_image, cut=get_com(auto_structures["Auto_Lung"]))
vis.add_contour({struct: auto_structures[struct] for struct in auto_structures.keys()})
fig = vis.show()

plt.savefig(f"{output_directory}/{filename}/{filename}_lung_visualization.png")
plt.close(fig)
print(f"Visualization saved to: {output_directory}/{filename}/{filename}_lung_visualization.png")
