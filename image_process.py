from PIL import Image

img = Image.open('static/images/vi_portrait.png')
print(img.size)
img.thumbnail((300,300))
print(img.size)
img.save('vi_thumbnail.png')