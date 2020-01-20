import arrow
from PIL import Image

#Today's Date 
time = arrow.utcnow().format('MM/DD/YYYY')
print(time)

image1 = Image.open('image/paradise.jpg')
image1.rotate(180).save('image/paradise_rotate.jpg')

print("See rotated image in Image folder")


input("Press ENTER to quit!")
