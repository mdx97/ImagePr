import sys
import queue
from PIL import Image

MAX_DIFF = 200

def validPixel(pixel_matrix, pixel_coord, target_color):
    if (pixel_coord[0] < 0 or pixel_coord[1] < 0):
        return False
    if (pixel_coord[0] >= len(pixel_matrix) or pixel_coord[1] >= len(pixel_matrix[0])):
        return False
    
    pixel_color = pixel_matrix[pixel_coord[0]][pixel_coord[1]]
    total_diff = 0
    total_diff += abs(pixel_color[0] - target_color[0])
    total_diff += abs(pixel_color[1] - target_color[1])
    total_diff += abs(pixel_color[2] - target_color[2])
    
    if (total_diff > MAX_DIFF):
        return False

    return True

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
    pixel_coord = (-1, -1)
    for i in range(img.height):
        for j in range(img.width):
            if (R[i][j] == 0):
                pixel_coord = (i, j)
                break
    
    if (pixel_coord[0] != -1 and pixel_coord[1] != -1):
        base_color = I[pixel_coord[0]][pixel_coord[1]]
        region_pixels = [pixel_coord]

        # Use BFS to find adjacent pixels of similar color.
        q = queue.Queue()
        q.put(pixel_coord)
        
        while not q.empty():
            pixel = q.get()

            # Add adjacent pixels to q if they are valid.
            up_coord = (pixel[0] - 1, pixel[1])
            down_coord = (pixel[0] + 1, pixel[1])
            left_coord = (pixel[0], pixel[1] - 1)
            right_coord = (pixel[0], pixel[1] + 1)
            
            if (up_coord not in region_pixels and validPixel(I, up_coord, base_color)):
                region_pixels.append(up_coord)
                q.put(up_coord)
            if (down_coord not in region_pixels and validPixel(I, down_coord, base_color)):
                region_pixels.append(down_coord)
                q.put(down_coord)
            if (left_coord not in region_pixels and validPixel(I, left_coord, base_color)):
                region_pixels.append(left_coord)
                q.put(left_coord)
            if (right_coord not in region_pixels and validPixel(I, right_coord, base_color)):
                region_pixels.append(right_coord)
                q.put(right_coord)
       
        # Assign a mean color to this region and mark all pixels as a part of this region.
        sum_r = 0
        sum_g = 0
        sum_b = 0
        
        for pixel in region_pixels:
            R[pixel[0]][pixel[1]] = region
            pixel_color = I[pixel[0]][pixel[1]]
            sum_r += pixel_color[0]
            sum_g += pixel_color[1]
            sum_b += pixel_color[2]

        region_count = len(region_pixels)
        mean_color = (int(sum_r / region_count), int(sum_g / region_count), int(sum_b / region_count))
        C.append(mean_color)
        region += 1
    else:
        all_pixels_grouped = True

# Set pixel colors based off of mean.
for i in range(img.height):
    for j in range(img.width):
        region = R[i][j]
        color = C[region - 1]
        I[i][j] = color

# Save Image
new_img = Image.new("RGB", (img.width, img.height))
for i in range(img.height):
    for j in range(img.width):
        new_img.putpixel((j, i), I[i][j])

new_img.save("files/cartoon.jpg")