"""
File nam: new_image.py

Purpose: The goal is to take the item from the first picture and insert it over the top of the scene in the second picture.

"""
from PIL import Image
green_image = Image.open("cse110_images/cactus.jpg")
new_image = Image.open("cse110_images/beach.jpg")



pixel_new_image = new_image.load()

pixel_green_image = green_image.load()

for w in range(200,500):
    for h in range(10,570 ):
        (r, g, b) = pixel_green_image[w, h] 
        if r != 76 and g != 244 and b != 24 :
           pixel_new_image[w, h] = (r, g, b)
        
       

new_image.show()

new_image.save("new_image.jpg")
       
