import os
import pydicom

folder = r"C:\Users\HP\Downloads\tcga_stad\TCGA-VQ-A8DZ\93079\73997"

positions = []

for file in os.listdir(folder):
    if file.lower().endswith(".dcm"):

        path = os.path.join(folder, file)

        ds = pydicom.dcmread(path)

        z = ds.ImagePositionPatient[2]

        positions.append((file, z))

for file, z in positions:
    print(file, "->", z)

print("\nTotal slices:", len(positions))