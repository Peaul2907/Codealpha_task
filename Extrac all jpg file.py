import os
import shutil
#write derictory of source folder and destimation folder.
source_folder = 'source_folder_path'
destination_folder = 'destination_folder_path'

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through files and move .jpg files
for file in os.listdir(source_folder):
    if file.lower().endswith('.jpg'):
        shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))
        print(f'Moved: {file}')