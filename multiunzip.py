import sys
import glob
import os
import zipfile

folder = sys.argv[1]
pattern = "*.zip"
files = glob.glob(os.path.join(folder, pattern))

for file in files:
    print(f"Unzipping {file}...")
    with zipfile.ZipFile(file, "r") as zip:
        zip.extractall(folder)

input()