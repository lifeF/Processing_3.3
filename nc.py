from PIL import Image
x=10
y=20
im = Image.open('hack.png') # Can be many different formats.
pix = im.load()
width,height = im.size
for y in range(height):
    for x in range(width):
        pix[x,y] = (200, 204, 202, 255)
print height 
print pix[x,y]  

im.save('map.png') 
