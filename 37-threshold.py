import image

img = image.Image("rooster.jpg")
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
        
        #filter logic goes here
        if r + g + b > 300:
            new_r = 255
            new_g = 255
            new_b = 255
        else:
            new_r = 0
            new_g = 0
            new_b = 0
        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)
    img.draw(canvas)
    
    