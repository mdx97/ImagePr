from PIL import Image

class PixelProfile:
    diff_top = 0
    diff_bot = 0
    diff_left = 0
    diff_right = 0

def color_diff(col1, col2):
    if (col1 == 0):
        col1 = 1
    if (col2 == 0):
        col2 = 1
    return (abs(col1 - col2) / ((col1 + col2) / 2)) * 100

def pixel_diff(pix1_val, pix2_val):
    diff_r = color_diff(pix1_val[0], pix2_val[0])
    diff_g = color_diff(pix1_val[1], pix2_val[1])
    diff_b = color_diff(pix1_val[2], pix2_val[2])
    return (diff_r + diff_g + diff_b) / 3

def outline(file, min_diff):
    img = Image.open(file)
    pixels = [[(0, 0, 0) for x in range(img.width)] for y in range(img.height)]

    for i in range(img.height):
        for j in range(img.width):
            pixels[i][j] = img.getpixel((j, i))

    profiles = [[PixelProfile() for x in range(img.width)] for y in range(img.height)]
    
    for i in range(img.height):
        for j in range(img.width):
            profile = PixelProfile()
            pixel_val = pixels[i][j]

            if (i > 0):
                profile.diff_top = pixel_diff(pixel_val, pixels[i - 1][j])
            if (i < len(pixels) - 1):
                profile.diff_bot = pixel_diff(pixel_val, pixels[i + 1][j])
            if (j > 0):
                profile.diff_left = pixel_diff(pixel_val, pixels[i][j - 1])
            if (j < len(pixels[i]) - 1):
                profile.diff_right = pixel_diff(pixel_val, pixels[i][j + 1])

            profiles[i][j] = profile

    for i in range(img.height):
        for j in range(img.width):
            profile = profiles[i][j]

            if (profile.diff_top >= min_diff):
                pixels[i + 1][j] = (0, 0, 0)
            if (profile.diff_bot >= min_diff):
                pixels[i - 1][j] = (0, 0, 0)
            if (profile.diff_left >= min_diff):
                pixels[i][j - 1] = (0, 0, 0)
            if (profile.diff_right >= min_diff):
                pixels[i][j + 1] = (0, 0, 0)

    new_img = Image.new("RGB", (img.width, img.height))

    for i in range(img.height):
        for j in range(img.width):
            new_img.putpixel((j, i), pixels[i][j])

    new_img.save("files/edit.jpg")

outline("files/pepsi.jpg", 15)