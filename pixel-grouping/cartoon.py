# Objective
# --------
# Main objective is to group pixels that are of similar color into regions. Then, create a mean color for the region. The region will then be filled with that color.
#
# --------
# Design
# --------
# * Building Regions *
# 1. Use the matrix representation of the image (I). Each pixel will be represented by a tuple containing RGB values. [(R, G, B)]
# 2. Use a second matrix to represent regions (called R). This matrix will be initialized with 0s. Regions will begin with the number 1.
# 3. We will define a list (C) which will store the colors for each region.
# 4. To detect our regions. We will pick the index of the first 0 in R. (This is the first pixel that is not a member of a region yet.)
# 5. Conduct a BFS on adjacent pixels. Use the the color of the pixel picked in step 3 to determine which pixels will be added to the region.
# 6. Set all the values for the selected pixels to the number of the region in R.
# 7. Average the color of all the pixels selected, add that value to C for the current region.
#
# * Building the New Image *
# 1. We will use the I matrix, since there is no need to create a new matrix. Loop through each pixel and get the region it is apart of from R. Then set the color of the pixel to the value cooresponding to the region selected from R from C.
# 2. Save the new image!

import sys
import queue
from PIL import Image

path = "files/" + sys.argv[1]
img = Image.open(path)

# Load the image into I - The matrix representing pixel RGB values.
I = [[(0, 0, 0) for x in range(img.width)] for y in range(img.height)]
for i in range(img.height):
    for j in range(img.width):
        I[i][j] = img.getpixel((j, i))

# Initialize R - The matrix representing which region each pixel belongs to.
R = [[0 for x in range(img.width)] for y in range(img.height)]

# Initialize C - This list will be used to store the mean color for each region.
C = []

all_pixels_grouped = False
region = 1

while (not all_pixels_grouped):
    # Find the first pixel which has not been assigned a region.
    pixel_coord = [-1, -1]
    for i in range(img.height):
        for j in range(img.width):
            if (R[i][j] == 0):
                pixel_coord = [i, j]
                break
    
    if (pixel_coord[0] != -1 and pixel_coord[1] != -1):
        region_pixels = []
        q = queue.Queue()
        q.put(tuple(pixel_coord))
        
        while not q.empty():
            pixel = q.get()
            region_pixels.append(pixel)

            # TODO: If adjacent pixels are close enough to main pixel color, add to queue.
            # Do not add to the queue if the coord is already in region_pixels.

        # TODO: Calculate mean color

        for pixel in region_pixels:
            R[pixel[0]][pixel[1]] = region
        
        C.append(mean_color)
        region += 1
    else:
        all_pixels_grouped = True

# Set pixel colors based off of mean.
for i in range(img.height):
    for j in range(img.width):
        region = R[i][j]
        color = C[region]
        I[i][j] = color

# Save Image
new_img = Image.new("RGB", (img.width, img.height))
for i in range(img.height):
    for j in range(img.width):
        new_img.putpixel((j, i), I[i][j])

new_img.save("files/cartoon.jpg")
