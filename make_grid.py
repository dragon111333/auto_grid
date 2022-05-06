import sys
from PIL import Image,ImageDraw,ImageFont
class DrawImage :
    @staticmethod
    def grid(_img,_area,debug=False):
        font = ImageFont.truetype("arial.ttf",8)
        img = Image.open(_img)
        draw = ImageDraw.Draw(img)
        print(f"width : {img.size[0]},height :{img.size[1]}")
        area = _area
        size = img.size[0]/area
        x=0
        y=0
        for col in range(0,(area+1)) :
            for row in range(0,area+1) :
                #for debug mode
                if(debug) :
                    draw.text((x+2,y+2),f"({row+1},{col+1})",font=font,fill="black")
                draw.rectangle([(x,y), (size, size)], outline="black")
                print(f"-->({row+1},{col+1})")
                x = x+size
            y = y+size
            x = 0
        img.show()
        img = img.save(f"new_{_img}")
        pass
if(__name__=="__main__") :
    img = "map.jpg"
    area = 400
    DrawImage.grid(img,area,debug=True)