#https://stackoverflow.com/questions/46666762/getting-dicom-structure-contours-as-array-in-python

import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

import os

import pydicom
ds = pydicom.read_file("rtstruct.dcm", force=True)
ds.dir("contour")

ctrs = ds.ROIContourSequence

# The data is stored (in this case, as is usual) as a set of coordinates 
# for each plane. To get the data for one contour, for one plane, you could use

ctrs[0].ContourSequence[0].ContourData

# These are triplets of (x, y, z) coordinates one after the other.
# You can find out more information about each contour (name, etc) in 
# the StructureSetROISequence sequence, for the index given by Referenced 
# ROI Number.
# You could get a complete array for all of these by looping through 
# each dataset in the ContourSequence for that particular contour and 
# appending them together into one array.
