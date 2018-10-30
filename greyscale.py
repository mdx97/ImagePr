# Usage: python greyscale.py <file>
import sys
from PIL import Image
from pr_common import *

file_name = sys.argv[1]
file_path = filePath(file_name)
img = Image.open(file_path)
pixels = pixelValues(img)

for i in range(img.height):
    for j in range(img.width):
        pixels[i][j] = greyValue(pixels[i][j])

savePixelsToImage(editedFilePath(file_name, "greyscale"), pixels)
