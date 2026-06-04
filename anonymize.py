import pydicom

# Path to the original DICOM file
input_file = r"C:\Users\HP\Downloads\tcga_stad\TCGA-VQ-A8DZ\93079\54420\0b1089ed-4128-4fbb-8ce3-3a3397c4f2d1.dcm"

# Name of the anonymized output file
output_file = r"anonymized.dcm"

# Read DICOM
ds = pydicom.dcmread(input_file)

# ==========================
# ANONYMIZE SENSITIVE FIELDS
# ==========================

ds.PatientName = "ANON"
ds.PatientID = "ANON"

# Only modify if the field exists
if "PatientSex" in ds:
    ds.PatientSex = "O"

if "PatientAge" in ds:
    ds.PatientAge = "000Y"

if "AccessionNumber" in ds:
    ds.AccessionNumber = "ANON"

# Remove dates
for field in [
    "StudyDate",
    "SeriesDate",
    "AcquisitionDate",
    "ContentDate"
]:
    if field in ds:
        ds.data_element(field).value = ""

# Remove times
for field in [
    "StudyTime",
    "SeriesTime",
    "AcquisitionTime",
    "ContentTime"
]:
    if field in ds:
        ds.data_element(field).value = ""

# ==========================
# SAVE NEW FILE
# ==========================

ds.save_as(output_file)

print("Anonymization complete!")
print("Saved as:", output_file)

# ==========================
# VERIFY CHANGES
# ==========================

new_ds = pydicom.dcmread(output_file)

print("\n--- Verification ---")
print("Patient Name:", new_ds.get("PatientName", "N/A"))
print("Patient ID:", new_ds.get("PatientID", "N/A"))
print("Patient Sex:", new_ds.get("PatientSex", "N/A"))
print("Patient Age:", new_ds.get("PatientAge", "N/A"))
print("Accession Number:", new_ds.get("AccessionNumber", "N/A"))
print("Study Date:", new_ds.get("StudyDate", "N/A"))