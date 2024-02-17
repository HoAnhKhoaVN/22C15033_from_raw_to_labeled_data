import argparse
import os
from typing import Text, List

class GetLabel(object):
    def __init__(
        self,
        path: Text,
        start: int,
        end: int,
    )-> None:
        self.path = path
        self.start = start
        self.end = end
        self.set_valid_index = range(
            self.start,
            self.end + 1
        )
        self.data = self.get_data()                
    
    def get_data(self)-> List[Text]:
        """"""
        res = []
        with open(self.path, 'r', encoding= 'utf-8') as f:
            for line in f:
                path, _  = line.split('\t')
                basename = os.path.basename(path)
                index = int(basename.split('__')[-1].split('.')[0])
                if index in self.set_valid_index:
                    res.append(line)

        res = sorted(
            res,
            key = lambda path: int(os.path.basename(path).split('__')[-1].split('.')[0])
        )
        print(f'Length res: {len(res)}')
        print(f'Top 1: {res[0]}')
        return res
    
    def save(
        self,
        new_path : Text
    )-> None:
        """"""
        with open(new_path, 'w', encoding='utf-8') as f:
            for line in self.data:
                f.write(f'{line}')
    

if __name__ == '__main__':
    # PATH = 'xi_mang_go/xi_mang/Label.txt'
    # NEW_PATH = 'xi_mang_go/labeled/xi_mang/1k/Label_1k.txt'
    # START = 1
    # END =  1000

    # region get argument
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-lb', 
        '--label_txt',  
        help="Path to Label.txt."
    )

    parser.add_argument(
        '-nlb', 
        '--new_label_txt',  
        help="Path new label path."
    )

    parser.add_argument(
        '-s', 
        '--start',  
        help="Start index"
    )

    parser.add_argument(
        '-e', 
        '--end',  
        help="End index"
    )src/zip_file.py

    args = parser.parse_args()
    # endregon


    obj = GetLabel(
        path = args.label_txt,
        start = args.start,
        end = args.end
    )

    obj.save(args.new_label_txt)