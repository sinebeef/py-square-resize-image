#!/usr/bin/python3
import json,  os,    sys,   time
from   PIL    import Image
from   shutil import copyfile

PRODUCTS  = [   {"image_filename":"ADJBEV180BN_206830.gif"},
                {"image_filename":"ADJSQ0370RB_206786.gif"},
                {"image_filename":"SSP8CH_18314.gif"}
]
IMAGE_DIR = '/cygdrive/c/Users/sine/Dropbox/github/py-square-resize-image/old/'
NEW_DIR = '/cygdrive/c/Users/sine/Dropbox/github/py-square-resize-image/new/'
#PRODUCTS  = json.load(open(sys.argv[1]))
#IMAGE_DIR = sys.argv[2]
#NEW_DIR = sys.argv[3]

done     = set()
no_image = set()

for product in PRODUCTS:

    # if image filename exists
    if product['image_filename']:
 
        copyfile(
            os.path.join(IMAGE_DIR, product['image_filename']), 
            os.path.join(NEW_DIR, product['image_filename'])
        )
 
        # filename references the copied IMAGE
        filename = os.path.join(NEW_DIR, product['image_filename'])        
        image = Image.open(filename)
        width, height = image.size
        
        if width != height:
        
            bigside = width if width > height else height
            squared = Image.new('RGB', (bigside, bigside), (255, 255, 255, 255))
            offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))
            squared.paste(image, offset)
            
            # save newly squared image
            squared.save(filename)

        # filename references the copied IMAGE
        filename = os.path.join(NEW_DIR, product['image_filename'])        
        image = Image.open(filename)
        width, height = image.size            
        if width < 300:
                
            # resize and save image
            if image.format == 'JPEG':
                image = image.resize((300,300), image.LANCZOS)
                image.save(filename)
            else:
                image = image.resize((300,300))
                image.save(filename)

    else:
        no_image.add(product['product_number'])

for _id in list(no_image):
    print('WARNING: No Image Found:', _id)
