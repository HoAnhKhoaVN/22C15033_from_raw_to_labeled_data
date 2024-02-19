import os

GOOD_FD = 'D:/Master/OCR_Nom/fulllow_ocr_temple/dataset/labeling/sence_text/xi_mang_go/labeled/xi_mang/1k/img/good_fd'
TEST_PATH= 'D:/Master/OCR_Nom/fulllow_ocr_temple/dataset/labeling/sence_text/xi_mang_go/labeled/xi_mang/1k/test.txt'
TEST_FD = 'D:/Desktop/testset/xi_mang/img'

if __name__ == '__main__':
    with open(TEST_PATH, 'r', encoding = 'utf-8') as f:
        for line in f:
            path, _  = line.split('\t')
            basename = os.path.basename(path)
            src = os.path.join(
                GOOD_FD,
                basename
            )
            tgt = os.path.join(
                TEST_FD,
                basename
            )

            os.system(f'cp {src} {tgt}')
