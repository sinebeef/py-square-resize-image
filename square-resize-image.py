#!/usr/bin/python3
import json,  os,    sys,   time
from   PIL    import Image
from   shutil import copyfile

PRODUCTS  = json.load(open(sys.argv[1]))
IMAGE_DIR = sys.argv[2]
NEW_DIR = sys.argv[3]
STAMP = time.strftime('%H%M%S')

done     = set()
no_image = set()

for product in PRODUCTS:
    if product['image_filename']:
        filename = os.path.join(IMAGE_DIR, product['image_filename'])
        image = Image.open(filename)
        width, height = image.size

        if width != height:
            bigside = width if width > height else height
            background = Image.new('RGB', (bigside, bigside), (255, 255, 255, 255))
            offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))
            background.paste(image, offset)
            background.save(filename)

        copyfile(
            os.path.join(IMAGE_DIR, product['image_filename']), 
            os.path.join(NEW_DIR, product['product_image'])
        )
        #print('CREATE:', os.path.join(IMAGE_DIR, product['product_image']))
        done.add(product['image_filename'])
    else:
        no_image.add(product['product_number'])

#for filename in list(done):
    #print('DONE:', filename)
    #os.remove(os.path.join(IMAGE_DIR, filename))

for _id in list(no_image):
    print('WARNING: No Image Found:', _id)