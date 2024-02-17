import os
from typing import Text, Tuple

GOOD_FD = 'good_fd'
BAD_FD = 'bad_fd'
IMG_TYPE = [
    'jpg',
    'png',
    'jpeg'
]

class FilterImage(object):
    def __init__(
        self,
        label_path: Text,
        img_path: Text
    )-> None:
        self.label_path = label_path
        self.img_path = img_path
        self.img_good_path = os.path.join(self.img_path, GOOD_FD)
        self.img_bad_path = os.path.join(self.img_path, BAD_FD)
        self.create_folder()

        
    def create_folder(self)->None:
        """"""
        os.makedirs(self.img_good_path, exist_ok= True)
        os.makedirs(self.img_bad_path, exist_ok= True)

    def move_good_img(self)->None:
        """"""
        with open(self.label_path, 'r', encoding= 'utf-8') as f:
            for line in f:
                path, _  = line.split('\t')
                basename = os.path.basename(path)
                src = os.path.join(
                    self.img_path,
                    basename
                )
                tgt = os.path.join(
                    self.img_good_path,
                    basename
                )

                os.system(f'mv {src} {tgt}')
    
    def move_bad_img(self)->None:
        """"""
        for fn in os.listdir(self.img_path):
            if fn.split('.')[-1].lower() in IMG_TYPE:
                src = os.path.join(
                    self.img_path,
                    fn
                )
                tgt = os.path.join(
                    self.img_bad_path,
                    fn
                )

                os.system(f'mv {src} {tgt}')

    def __call__(self):
        """"""
        print("### MOVE GOOD IMAGE ###")
        self.move_good_img()

        print("### MOVE BAD IMAGE ###")
        self.move_bad_img()

if __name__ == '__main__':
    LABEL_PATH = 'xi_mang_go/labeled/xi_mang/1k/Label_1k.txt'
    IMG_PATH = 'xi_mang_go/labeled/xi_mang/1k/img'
    obj = FilterImage(
        label_path = LABEL_PATH,
        img_path = IMG_PATH
    )

    obj()