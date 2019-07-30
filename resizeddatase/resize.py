from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir,width=512,height=512):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
for jpgfile in glob.glob("/*.jpg"):#图片获取路径
    convertjpg(jpgfile,"/datase/train_resized/")#resize后图片保存路径
