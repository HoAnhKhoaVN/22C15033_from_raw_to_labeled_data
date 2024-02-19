import os

if __name__ == "__main__":
    INPUT_FOLDER_PATH = 'D:\\Desktop\\testset_238'
    FILENAME = os.path.join(
        INPUT_FOLDER_PATH,
        'fileState.txt'
    )
    with open(f'{FILENAME}', 'w', encoding='utf-8') as f:
        for fn in os.listdir(INPUT_FOLDER_PATH):
            f.write(f'{os.path.join(INPUT_FOLDER_PATH, fn)}\t1\n')
