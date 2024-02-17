import os
from typing import Text, List
from tqdm import tqdm

GOOD_FD = 'good_fd'
BAD_FD = 'bad_fd'
IMG_TYPE = [
    'jpg',
    'png',
    'jpeg'
]

class MatchImgWithLabel(object):
    def __init__(
        self,
        label_path: Text,
        img_path: Text
    )-> None:
        self.label_path = label_path
        self.img_path = img_path
        self.lst_fn = os.listdir(self.img_path)
        self.base_fd = os.path.basename(self.img_path)
        self.data = self.read_data()

    def read_data(self)->List[Text]:
        """"""
        with open(self.label_path, 'r', encoding= 'utf-8') as f:
            data = f.readlines()

        return data

    def __call__(self):
        """"""
        res = []
        for line in tqdm(self.data, desc = 'Progress match image with label: '):
            path, bb  = line.split('\t')
            basename = os.path.basename(path)
            if basename in self.lst_fn:
                res.append(f"{self.base_fd}/{basename}\t{bb}")
        

        with open(self.label_path, 'w', encoding='utf-8') as f:
            for line in res:
                f.write(f'{line}')


if __name__ == '__main__':
    LABEL_PATH = 'xi_mang_go/labeled/xi_mang/1k/Label_1k.txt'
    IMG_PATH = 'xi_mang_go/labeled/xi_mang/1k/img/good_fd'
    obj = MatchImgWithLabel(
        label_path = LABEL_PATH,
        img_path = IMG_PATH
    )

    obj()