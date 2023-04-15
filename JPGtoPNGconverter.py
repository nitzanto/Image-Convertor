import sys
import os
from PIL import Image

# Grabbing the first and second argument
# This folder will contain the converted images to PNG
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Checking if the output folder already exists, otherwise creates a new one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for fileName in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{fileName}')
    clean_name = os.path.splitext(fileName)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('Converted an Image')
