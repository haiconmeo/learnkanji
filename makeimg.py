from PIL import Image, ImageDraw
 
# def show_img(kanji)
img = Image.new('RGB', (500, 500), color = (73, 109, 137))

d = ImageDraw.Draw(img)
d.text((10,10), "Hello World", fill=(255,255,0))
 
img.show()