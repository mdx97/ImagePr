from PIL import Image

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