from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import os
def getpic(name, symp, dis):
    font = ImageFont.truetype('calibri.ttf',30)
    img = Image.open('medreport.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(310,680),text= name ,fill=(0,0,0),font=font)
    draw.text(xy=(299,825),text= symp ,fill=(0,0,0),font=font)
    draw.text(xy=(285,940),text= dis ,fill=(0,0,0),font=font)
    img.save('C:/Users/amree/Desktop/pictures.jpg') 