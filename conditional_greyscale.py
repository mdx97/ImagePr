import sys
from PIL import Image
from pr_common import *

def generalizedColor(pixel_val):
    color = "R"
    max_val = pixel_val[0]

    if (pixel_val[1] > max_val):
        max_val = pixel_val[1]
        color = "G"
    if (pixel_val[2] > max_val):
        color = "B"

    return color

file_name = sys.argv[1]
ignore_col = str(sys.argv[2])
img = getImage(file_name)
pixels = pixelValues(img)

for i in range(img.height):
    for j in range(img.width):
        pixel_val = pixels[i][j]
        general_color = generalizedColor(pixel_val)

        if (general_color != ignore_col):
            pixels[i][j] = greyValue(pixel_val)

savePixelsToImage(editedFilePath(file_name, "cond_greyscale"), pixels)

