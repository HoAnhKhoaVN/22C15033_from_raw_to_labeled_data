#python3 split_image -lb test.txt -s 'good_fd' -t 'test'

import argparse
import os
from typing import Text

class SplitImage(object):
    def __init__(
        self,
        label_path: Text,
        src_img: Text,
        tgt_img : Text
    )-> None:
        self.label_path = label_path
        self.src_img = src_img
        self.tgt_img = tgt_img

    def __call__(self):
        """"""
        with open(self.label_path, 'r', encoding = 'utf-8') as f:
            for line in f:
                path, _  = line.split('\t')
                basename = os.path.basename(path)
                src = os.path.join(
                    self.src_img,
                    basename
                )
                tgt = os.path.join(
                    self.tgt,
                    basename
                )

                os.system(f'cp {src} {tgt}')
        
        
if __name__ == '__main__':
    # region get argument
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-lb', 
        '--label_txt',  
        help="Path to Label.txt."
    )

    parser.add_argument(
        '-s', 
        '--src_img',  
        help="Path to source images."
    )

    parser.add_argument(
        '-t', 
        '--tgt_img',  
        help="Path to target images."
    )
    args = parser.parse_args()
    # endregon
    obj = SplitImage(
        label_path = args.label_txt,
        src_img = args.src_img,
        tgt_img = args.tgt_img,
    )

    obj()