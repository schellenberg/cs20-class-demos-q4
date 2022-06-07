import image

img = image.Image("sneakers.jpg")
width = img.get_width()
height = img.get_height()

canvas = image.ImageWin(width, height)
img.draw(canvas)

for x in range(width):
    for y in range(height):
        this_pixel = img.get_pixel(x, y)
        
        #get the current RGB values
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        new_pixel = image.Pixel(r-100, g-100, b-100)
        img.set_pixel(x, y, new_pixel)
    img.draw(canvas)
    
    