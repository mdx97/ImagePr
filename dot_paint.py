# Turn an image into the style of an oboriginal dot painting.
# K-means?
import sys
from PIL import Image
from pr_common import filePath, pixelValues, savePixelsToImage, editedFilePath

file_name = sys.argv[1]
file_path = filePath(file_name)
img = Image.open(file_path)
pixels = pixelValues(img)

img_sum_r = 0
img_sum_g = 0
img_sum_b = 0

for i in range(img.height):
    for j in range(img.width):
        pixel_val = pixels[i][j]
        img_sum_r += pixel_val[0]
        img_sum_g += pixel_val[1]
        img_sum_b += pixel_val[2]

total_pixels = img.height * img.width
background = (img_sum_r // total_pixels, img_sum_g // total_pixels, img_sum_b // total_pixels)

circle_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

circle_size = len(circle_matrix)

for i in range(0, img.height - (img.height % circle_size), circle_size):
    for j in range(0, img.width - (img.width % circle_size), circle_size):
        section_sum_r = 0
        section_sum_g = 0
        section_sum_b = 0
        sum_pixels = 0

        for k in range(0, circle_size):
            for l in range(0, circle_size):
                if (circle_matrix[k][l] == 0):
                    pixels[i + k][j + l] = background
                else:
                    pixel_val = pixels[i + k][j + l]
                    section_sum_r += pixel_val[0]
                    section_sum_g += pixel_val[1]
                    section_sum_b += pixel_val[2]
                    sum_pixels += 1
        
        section_avg_r = section_sum_r // sum_pixels
        section_avg_g = section_sum_g // sum_pixels
        section_avg_b = section_sum_b // sum_pixels
        avg_pixel_val = (section_avg_r, section_avg_g, section_avg_b)

        for k in range(0, circle_size):
            for l in range(0, circle_size):
                if (circle_matrix[k][l] != 0):
                    pixels[i + k][j + l] = avg_pixel_val

savePixelsToImage(editedFilePath(file_name, "dot_paint"), pixels)