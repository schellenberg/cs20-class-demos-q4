import image

width = 600
height = 400

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

for y in range(height):
    for x in range(width):
        this_pixel = image.Pixel(255, 0, 0)
        img.set_pixel(x, y, this_pixel)

    img.draw(canvas)