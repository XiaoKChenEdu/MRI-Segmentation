#!/usr/bin/python3

import os
import platipy # https://pyplati.github.io/platipy/index.html

from matplotlib import pyplot as plt

import SimpleITK as sitk

from platipy.imaging.projects.cardiac.run import run_hybrid_segmentation
from platipy.imaging import ImageVisualiser
from platipy.imaging.label.utils import get_com

### Change this ###
filename = f'volume_{1}'
### Change this ###

os.makedirs(f"./output/{filename}", exist_ok=True)
test_image = sitk.ReadImage(f"./input/volumes/{filename}.nii.gz")
auto_structures, _ = run_hybrid_segmentation(test_image)

output_directory = './output'

for struct_name in list(auto_structures.keys()):
    sitk.WriteImage(auto_structures[struct_name], str(f"{output_directory}/{filename}/{filename}_{struct_name}.nii.gz"))

print(f"Segmentations saved to: {output_directory}")

vis = ImageVisualiser(test_image, cut=get_com(auto_structures["Heart"]))
vis.add_contour({struct: auto_structures[struct] for struct in auto_structures.keys()})
fig = vis.show()

plt.savefig(f"{output_directory}/{filename}/{filename}_heart_visualization.png")
plt.close(fig)
print(f"Visualization saved to: {output_directory}/{filename}/{filename}_heart_visualization.png")
