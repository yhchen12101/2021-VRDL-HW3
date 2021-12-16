import cv2
from PIL import Image
import pycococreatortools as cocotools
import os


path = 'train/'
train_path = './train.json'

def write_names(f, dirs):
    id = 0
    first = True
    f.write('\"images\":\n')
    f.write('[\n')
    for image_dir in dirs:
        for file in os.listdir(image_dir):
            if file[-3:] == 'png':
                if first is False:
                    f.write(',\n')
                else:
                    first = False
                img = Image.open(image_dir + '/' + file)
                image_size = [img.width, img.height]
                file_name = image_dir + '/' + file
                info = cocotools.create_image_info(id, file_name, image_size)
                info = str(info)
                info = info.replace("\'", "\"")
                f.write(info)
                id += 1
    f.write('\n],\n')

def write_bbox_seg(f, dirs):
    f.write('\"annotations\":\n[\n')
    anno_id = 0
    first = True
    img_id = 0
    for mask_dir in dirs:
        for file in os.listdir(mask_dir):
            if file[-3:] == 'png':
                if first is False:
                    f.write(',\n')
                else:
                    first = False
                img = cv2.imread(mask_dir + '/' + file, cv2.IMREAD_GRAYSCALE)
                img = img / 255
                c_info = {}
                c_info["id"] = 1
                c_info["is_crowd"] = False
                anno = cocotools.create_annotation_info(anno_id, img_id,c_info, img)
                anno = str(anno)
                anno = anno.replace("\'", "\"")
                f.write(anno)
                anno_id += 1
        img_id += 1
    f.write('\n],\n')

def write_classes(f):
    f.write('\"categories\":\n')
    f.write('[\n')
    f.write('{\"id\": 1, \"name\": \"1\"}\n')
    f.write(']\n')


f1 = open(train_path, 'w')

img_names = os.listdir(path)

mask_dirs = []
image_dirs = []

for img_name in img_names:
    if img_name[0] == '.':
        continue
    mask_dir = path + img_name + '/masks'
    mask_dirs.append(mask_dir)
    image_dir = path + img_name + '/images'
    image_dirs.append(image_dir)


f1.write('{\n')
write_names(f1, image_dirs)
write_bbox_seg(f1, mask_dirs)
write_classes(f1)
f1.write('}\n')
