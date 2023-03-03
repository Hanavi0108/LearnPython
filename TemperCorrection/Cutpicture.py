# For Picture cutting 1920x1080
# author: Nanze

from PIL import Image

img = Image.open("1.jpg")
print(img.size)
cropped1 = img.crop((0, 0, 720, 600))  # (left, upper, right, lower)
cropped2 = img.crop((0, 500, 720, 800))
cropped3 = img.crop((0, 600, 720, 1100))
cropped4 = img.crop((0, 900,720, 1300))
cropped5 = img.crop((0, 1200,720, 1440))
cropped1.save("./cut1.jpg")
cropped2.save("./cut2.jpg")
cropped3.save("./cut3.jpg")
cropped4.save("./cut4.jpg")
cropped5.save("./cut5.jpg")
print(cropped3.size)

