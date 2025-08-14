import os
import shutil

path = r"C:/Users/adbou/Desktop/python/Automated file sorter/"
folders = {
    ".csv": "csv files",
    ".txt": "txt files",
    ".jpg": "image files",
    ".png": "image files"
}

for folder in set(folders.values()):
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        print(f"Creating folder: {folder_path}")
        os.makedirs(folder_path)

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path): 
        _, ext = os.path.splitext(file)
        ext = ext.lower()
        if ext in folders:
            dest_folder = os.path.join(path, folders[ext])
            shutil.move(file_path, os.path.join(dest_folder, file))
            print(f"Moved: {file} → {dest_folder}")
