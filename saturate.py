import sys
from PIL import Image
from pr_common import *

file_name = sys.argv[1]
saturation_color = sys.argv[2]
saturation_modifier = int(sys.argv[3])

img = getImage(file_name)
pixels = pixelValues(img)

for i in range(img.height):
    for j in range(img.width):
        pixel_val = pixels[i][j]
        color_idx = None

        if (saturation_color == "R"):
            color_idx = 0
        elif (saturation_color == "G"):
            color_idx = 1
        elif (saturation_color == "B"):
            color_idx = 2

        color_val = pixel_val[color_idx] + saturation_modifier
        
        if (color_val > 255):
            color_val = 255
        
        pixel_list = list(pixel_val)
        pixel_list[color_idx] = color_val
        pixels[i][j] = tuple(pixel_list)

savePixelsToImage(editedFilePath(file_name, "saturated"), pixels)
        