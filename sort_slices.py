import os
import pydicom

folder = r"C:\Users\HP\Downloads\tcga_stad\TCGA-VQ-A8DZ\93079\73997"

slices = []

for file in os.listdir(folder):
    if file.lower().endswith(".dcm"):

        path = os.path.join(folder, file)

        ds = pydicom.dcmread(path)

        z = float(ds.ImagePositionPatient[2])

        slices.append((file, z))

# Sort by z position
slices.sort(key=lambda x: x[1])

print("First 5 slices:")
for item in slices[:5]:
    print(item)

print("\nLast 5 slices:")
for item in slices[-5:]:
    print(item)