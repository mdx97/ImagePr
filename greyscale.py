from PIL import Image
from pr_common import pixelValues, savePixelsToImage

file_path = "files/linux_vm.jpg"
img = Image.open(file_path)
pixels = pixelValues(img)

def colorAverage(pixel_val):
    return (pixel_val[0] + pixel_val[1] + pixel_val[2]) // 3

def greyValue(pixel_val):
    grey_mag = colorAverage(pixel_val)
    return (grey_mag, grey_mag, grey_mag)

for i in range(img.height):
    for j in range(img.width):
        pixels[i][j] = greyValue(pixels[i][j])

savePixelsToImage("files/greyscale.jpg", pixels)
