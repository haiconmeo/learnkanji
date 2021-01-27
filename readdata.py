# import json
from PIL import Image, ImageDraw,ImageFont
import random

# data =[]
# with open("kanji/kanji-jouyou.json", "rt", encoding="utf-8") as fp:
#     input = json.load(fp)
    
#     for i in input:
#         data.append((i,input[i]['meanings'],input[i]['readings_on'],input[i]['readings_kun']))
def show_kanji(data):

    input = random.choice(data)
    img = Image.new('RGB', (800, 500), color = (73, 109, 137))
    font=ImageFont.truetype("Arial Unicode MS.ttf",50)
    mean = ImageFont.truetype("Arial Unicode MS.ttf",20)
    d = ImageDraw.Draw(img)
    d.text((10,10), input[0], fill=(255,255,0),font=font)
    for k in range(len(input[1])):
        d.text((100*(k+1),30), input[1][k], fill=(255,255,0),font=mean)
    d.text((10,200), 'on:', fill=(255,255,0),font=font)
    for k in range(len(input[2])):
        d.text((110*(k+1),230), input[2][k]+'|', fill=(255,255,0),font=mean)
    d.text((10,300), 'kun:', fill=(255,255,0),font=font)
    for k in range(len(input[3])):
        d.text((110*(k+1),330), input[3][k]+'|', fill=(255,255,0),font=mean)


    img.show()


