from PIL import Image

img = Image.open("files/test_pic.jpg")
print(img.getpixel((0, 0)))