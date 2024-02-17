#python3 src/zip_file.py --root D:/Master/OCR_Nom/fulllow_ocr_temple/dataset/labeling/sence_text/xi_mang_go/labeled/xi_mang/1k

import os
from typing import Text
import argparse
import shutil

class ZipFolder(object):
    def __init__(
        self,
        root: Text
    ) -> None:
        self.root = root

    def __call__(self) -> None:
        zip_name = os.path.basename(self.root)
        zip_dir = os.path.dirname(self.root)
        zip_path= os.path.join(zip_dir, zip_name)

        shutil.make_archive(
            base_name= zip_path,
            format= 'zip',
            root_dir= self.root,
            verbose= True
        )
                
if __name__ == "__main__":
    # region 1: Get argument
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-r', 
        '--root', 
        help="Path to folder contain txt file"
    )

    args = parser.parse_args()
    # endregion

    # region 2: Zip folder
    obj = ZipFolder(root = args.root)
    obj()

    # endregion