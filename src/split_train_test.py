import os
from typing import Text, List
from tqdm import tqdm
from sklearn.model_selection import train_test_split

class SplitTrainValTest(object):
    def __init__(
        self,
        label_path: Text,
    )-> None:
        self.label_path = label_path
        self.data = self.read_data()

    def read_data(self)->List[Text]:
        """"""
        with open(self.label_path, 'r', encoding= 'utf-8') as f:
            data = f.readlines()

        return data

    def write_data(
        self,
        data: List[Text],
        noti: Text
    )-> None:
        """"""
        # region 1: Get name
        dirname = os.path.dirname(self.label_path)
        new_path = os.path.join(dirname, f'{noti}.txt')

        # endregion

        # region 2: Write file
        with open(new_path, 'w', encoding='utf-8') as f:
            for line in tqdm(data, desc = f'Progress to save {noti}: '):
                f.write(f'{line}')

        # endregion

    def __call__(self):
        """"""
        # region 1: Split train
        train, another = train_test_split(
            self.data,
            test_size= 0.3,
            shuffle= True,
            random_state= 2103
        )

        # endregion

        # region 2: Split validation and testset
        val, test = train_test_split(
            another,
            test_size= 0.5,
            shuffle= True,
            random_state= 2103
        )

        # endregion

        # region 3: Write file
        self.write_data(data= train, noti= "train")
        self.write_data(data= val, noti= "val")
        self.write_data(data= test, noti= "test")
        # endregion
        
if __name__ == '__main__':
    LABEL_PATH = 'xi_mang_go/labeled/xi_mang/1k/Label_1k.txt'
    obj = SplitTrainValTest(
        label_path = LABEL_PATH,
    )

    obj()