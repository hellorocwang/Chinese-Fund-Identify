import os
from random import randint
path = '/home/wzp/table/numbers'

def get_label_dict():
    num_word = {}
    word_num = {}
    start = 0
    fo = open(path + '/label')
    for line in fo.readlines():
        word_num[line.strip('\n')] = start
        num_word[start] = line.strip('\n')
        start += 1
    return num_word, word_num
    
num_word, word_num = get_label_dict()

from PIL import Image,ImageDraw,ImageFont
import numpy as np
import cv2
from random import randint

def generate_picture(num_word, font_path, save_path):
    for p,q in num_word.items():
        picture_name = 0
        print(p)
        if not (os.path.exists(save_path + '/' + str(p))):
            os.mkdir(save_path + '/' + str(p))
        for i in range (0,150):
            for file in os.listdir(font_path):
                ran_size = randint(16,21)
                ran_start_left = float(randint(-200,200))/100
                ran_start_right = float(randint(-100,100))/100
                img = Image.new("L", (ran_size, ran_size), "white")
                draw = ImageDraw.Draw(img)
                font_size = ran_size + randint(-2,1)
                font = ImageFont.truetype(font_path + '/' + file, font_size)
                draw.text((ran_start_left, ran_start_right), q, fill = "black", font = font)
                im2 = np.asarray(img)
                im3 = np.uint8(im2)
                im4 = cv2.resize(im3, (30, 30), interpolation = cv2.INTER_NEAREST)            
                im5 = im4.copy()
                thresh = randint(175,195)
                im5[im5<thresh] = 0
                im5[im5>=thresh] = 255
                cv2.imwrite(save_path + '/' + str(p) + '/' + str(picture_name) + '.png',im5)
                picture_name += 1
                
font_path = '/home/wzp/table/numbers/font'
save_path = '/home/wzp/table/numbers/nums'

generate_picture(num_word, font_path, save_path)