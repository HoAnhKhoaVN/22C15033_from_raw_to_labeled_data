import os
from typing import Text, Dict
import json
from tqdm import tqdm

LABEL_PATH = 'Label.txt'
FILE_STATE= 'fileState.txt'
JSON_PATH = 'old2new.json'
TYPE_IMG = [
    'jpg',
    'png',
    'jpeg'
]

class Rename(object):

    def __init__(
        self,
        fd_path: Text
    )-> None:
        self.fd_path = fd_path
        self.label_path = os.path.join(
            self.fd_path,
            LABEL_PATH
        )
        self.file_state = os.path.join(
            self.fd_path,
            FILE_STATE
        )

        self.new_label_path = os.path.join(
            self.fd_path,
            f'new_{LABEL_PATH}'
        )
        self.new_file_state = os.path.join(
            self.fd_path,
            f'new_{FILE_STATE}'
        )

        self.old_label_path = os.path.join(
            self.fd_path,
            f'old_{LABEL_PATH}'
        )
        self.old_file_state = os.path.join(
            self.fd_path,
            f'old_{FILE_STATE}'
        )
        self.json_path : Dict = os.path.join(
            self.fd_path,
            JSON_PATH
        )

        self.old2new = self.get_mapping()

    def get_mapping(self):
        """"""
        # region 1: Get list of old file
        lst_old_fn = os.listdir(path = self.fd_path)
        lst_old_fn = list(filter(lambda x: x.split('.')[-1].lower() in TYPE_IMG, lst_old_fn))
        print(f'Set extension: {set(list(map(lambda x: x.split(".")[-1].lower(), lst_old_fn)))}')
        # endregion
        

        basename = os.path.basename(self.fd_path)
        num_file = len(lst_old_fn)

        lst_new_fn = list(map(lambda x: f'{basename}__{str(x+1).zfill(7)}.jpg', range(num_file)))

        old2new = dict(zip(lst_old_fn, lst_new_fn))
        
        with open(self.json_path, 'w', encoding= 'UTF-8') as f:
            json.dump(
                obj= old2new,
                fp = f,
                ensure_ascii= True,
                indent= 4
            )
        
        return old2new

    def rename_label_txt(self)-> None:
        """"""
        with open(self.label_path, 'r', encoding= 'UTF-8-sig') as fr:
            data = fr.readlines()
        
        # Create dictionay with file name and list of bbox
            
        dirname = os.path.basename(self.fd_path)

        with open(self.new_label_path, 'w', encoding='UTF-8-sig') as fw:
            for line in tqdm(data, desc = "Progress for rename in Label.txt: " ):
                fn, bbox = line.split('\t')
                old_fn = os.path.basename(fn)
                new_fn = self.old2new.get(old_fn, '')

                if new_fn:
                    fw.write(f'{dirname}/{new_fn}\t{bbox}')

    def rename_file_state(self)-> None:
        """"""
        with open(self.file_state, 'r', encoding= 'UTF-8') as fr:
            data = fr.readlines()
        
        # Create dictionay with file name and list of bbox
        abspath = os.path.abspath(path= self.fd_path)
        with open(self.new_file_state, 'w', encoding='UTF-8') as fw:
            for line in tqdm(data, desc = "Progress for rename in fileState.txt: " ):
                fn, bbox = line.split('\t')
                old_fn = os.path.basename(fn)

                new_fn = self.old2new.get(old_fn, '')

                if new_fn:
                    fw.write(f'{abspath}\{new_fn}\t{bbox}')

    def rename_file(self):
        """"""
        os.system(
            command= f'mv {self.label_path} {self.old_label_path}'
        )

        os.system(
            command= f'mv {self.file_state} {self.old_file_state}'
        )

        os.system(
            command= f'mv {self.new_label_path} {self.label_path}'
        )

        os.system(
            command= f'mv {self.new_file_state} {self.file_state}'
        )

    def __call__(self) -> None:
        # region 1: Change name in folder
        for old, new in tqdm(self.old2new.items(), desc = "Progress for rename"):
            src = os.path.join(self.fd_path, old)
            tgt = os.path.join(self.fd_path, new)
            os.system(command=f'mv {src} {tgt}')

        # endregion

        # region 2: Change name in Label.txt
        self.rename_label_txt()
        
        # endregion

        # region 3: Change name in fileState.txt
        self.rename_file_state()

        # endregion

        # region 4: Post-process
        self.rename_file()

        # endregion

if __name__ == "__main__":
    FD_PATH = 'D:/Master/OCR_Nom/fulllow_ocr_temple/dataset/labeling/sence_text/xi_mang_go/xi_mang'

    obj = Rename(
        fd_path = FD_PATH
    )

    obj()
