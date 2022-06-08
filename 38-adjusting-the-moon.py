import image

img = image.Image("bird-far.jpg")

width = img.get_width()
height = img.get_height()

canvas = image.ImageWin(width, height)
img.draw(canvas)

for x in range(width):
    for y in range(height):
        this_pixel = img.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        #filter logic here
        if r + g + b >= 200:
            new_pixel = image.Pixel(255, 255, 255)
            img.set_pixel(x, y, new_pixel)
        
    img.draw(canvas)