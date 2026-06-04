import os
import pydicom
import numpy as np

folder = r"C:\Users\HP\Downloads\tcga_stad\TCGA-VQ-A8DZ\93079\73997"

slices = []

# Read all DICOM files
for file in os.listdir(folder):

    if file.lower().endswith(".dcm"):

        path = os.path.join(folder, file)

        ds = pydicom.dcmread(path)

        z = float(ds.ImagePositionPatient[2])

        slices.append((z, ds))

# Sort by position
slices.sort(key=lambda x: x[0])

# Extract image arrays
images = [s[1].pixel_array for s in slices]

# Stack into volume
volume = np.stack(images, axis=-1)

print("Volume created!")
print("Volume shape:", volume.shape)

import matplotlib.pyplot as plt

num_slices = volume.shape[2]

for i in range(num_slices):

    plt.imshow(volume[:, :, i], cmap="gray")
    plt.title(f"Slice {i+1}/{num_slices}")

    plt.show()  # close window to move to next slice