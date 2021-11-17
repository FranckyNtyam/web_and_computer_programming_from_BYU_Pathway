"""
File nam: new_image.py
Author: Ntyam Adjomo Francky Ludovic.

Purpose: The goal is to take the item from the first picture and insert it over the top of the scene in the second picture.

"""
print("Final Requirements\n")

from PIL import Image

# Variables contain green and background image.
green_image = Image.open("cse110_images/cactus.jpg")
new_image = Image.open("cse110_images/beach.jpg")


# Variables contain pixels of green and background image.
pixel_new_image = new_image.load()
pixel_green_image = green_image.load()

for w in range(200,475):
    """
     This loop iterate through all the pixels of the green image
     and set pixel in our new image to have the appropriate red, green, and blue value.
    """
    for h in range(10,550 ):
        (r, g, b) = pixel_green_image[w, h] 
        if r != 76 and g != 244 and b != 24 :
           pixel_new_image[w, h] = (r, g, b)
        
       
# display new image.
new_image.show()

# save the new image with jpg format. 
new_image.save("new_image.jpg")

print("END of Final Requirements\n")


print("----------------------------------\n")



print("Showing Creativity and Exceeding Requirements\n")

green_image = Image.open(input("write or past the name or path of green image of choice here:  "))

green_image.show()

new_image = Image.open(input("write or past the name or path of background image choice here:  "))      

new_image.show()

# Variables contain pixels of green and background image.
pixel_new_image = new_image.load()
pixel_green_image = green_image.load()

width = int(input("Enter the width zone you want to iterate: "))
height = int(input("Enter the height zone you want to iterate: "))

for w in range(width):
    """
     This loop iterate through all the pixels of the green image
     and set pixel in our new image to have the appropriate red, green, and blue value.
    """
    for h in range(height):
        (r, g, b) = pixel_green_image[w, h] 
        if r != 76 and g != 244 and b != 24 :
           pixel_new_image[w, h] = (r, g, b)

# display new image.
new_image.show()

# save the new image with jpg format. 
new_image.save("new_image.jpg")