from PIL import Image

# Pixel matrix functions
def pixelValues(img):
    pixels = [[(0, 0, 0) for x in range(img.width)] for y in range(img.height)]
    for i in range(img.height):
        for j in range(img.width):
            pixels[i][j] = img.getpixel((j, i))
    
    return pixels

def savePixelsToImage(file_path, pixels):
    img_h = len(pixels)
    img_w = len(pixels[0])
    new_img = Image.new("RGB", (img_w, img_h))

    for i in range(img_h):
        for j in range(img_w):
            new_img.putpixel((j, i), pixels[i][j])
    
    new_img.save(file_path)

# Greyscale functions
def colorAverage(pixel_val):
    return (pixel_val[0] + pixel_val[1] + pixel_val[2]) // 3

def greyValue(pixel_val):
    grey_mag = colorAverage(pixel_val)
    return (grey_mag, grey_mag, grey_mag)

# File path functions
def filePath(file_name):
    return "files/" + file_name

def editedFilePath(file_name, edit):
    return "files/{}_{}.jpg".format(removeExtension(file_name), edit)

def removeExtension(file_name):
    return file_name[0:file_name.index('.')]