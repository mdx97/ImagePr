# Usage: python greyscale.py <file>
import sys
from PIL import Image
from pr_common import *

file_name = sys.argv[1]
img = getImage(file_name)
pixels = pixelValues(img)

for i in range(img.height):
    for j in range(img.width):
        pixels[i][j] = greyValue(pixels[i][j])

savePixelsToImage(editedFilePath(file_name, "greyscale"), pixels)
