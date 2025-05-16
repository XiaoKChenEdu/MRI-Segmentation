#!/usr/bin/python3

import os
import platipy # https://pyplati.github.io/platipy/index.html

from matplotlib import pyplot as plt

import SimpleITK as sitk

from platipy.imaging.projects.cardiac.run import run_hybrid_segmentation
from platipy.imaging.projects.nnunet.run import run_segmentation
from platipy.imaging import ImageVisualiser
from platipy.imaging.label.utils import get_com

for i in range(0, 1):
    ### Change this ###
    filename = f'patient0-{i}0.0B'
    ### Change this ###

    os.makedirs(f"./output/{filename}", exist_ok=True)
    test_image = sitk.ReadImage(f"./input/patient/patient0/{filename}.nii.gz")
    auto_structures = run_segmentation(test_image)


    output_directory = './output'

    sitk.WriteImage(auto_structures["Struct_0"], str(f"{output_directory}/{filename}/{filename}_Heart.nii.gz"))

    print(f"Segmentations saved to: {output_directory}/{filename}")
