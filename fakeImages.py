from PIL import Image, ImageDraw

# Create an image (width=256, height=256) with random colors
img = Image.new('RGB', (256, 256), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Draw some random circles
for i in range(50):
    x, y = (i*5, i*5)
    draw.ellipse([x, y, x+30, y+30], fill=(i*5, 100, 200))

img.show()
img.save("fake_image.png")
