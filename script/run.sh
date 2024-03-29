# source 
##############
### CHANGE ###
##############
ROOT="D:/Master/OCR_Nom/fulllow_ocr_temple/dataset/labeling/sence_text/xi_mang_go/labeled/xi_mang/100"
LABEL_PATH='D:/Master/OCR_Nom/fulllow_ocr_temple/dataset/labeling/sence_text/xi_mang_go/xi_mang/Label.txt'
NEW_LABEL_PATH=$ROOT/Label_100.txt
IMG_PATH=$ROOT/img
START=1
END=100

##################
### END CHANGE ###
##################

echo "### 1. GET LABEL ###"
python3 src/get_label.py --label_txt $LABEL_PATH \
                         --new_label_txt $NEW_LABEL_PATH \
                         --start $START \
                         --end $END

echo "### 2. FILTER IMAGE ###"
python3 src/filter_image.py --label_txt $NEW_LABEL_PATH \
                           --img_path $IMG_PATH

echo "### 3. REMOVE DUPLICATE IMAGE ###"
GOOD_IMG="$IMG_PATH/good_fd"
find-dups $GOOD_IMG \
         --parallel \
         --progress \
         --on-equal delete-first \
         --hash-db hashes.json

echo "### 4. MATCH IMAGE WITH LABEL ###"

python3 src/match_image_with_label.py --label_txt $NEW_LABEL_PATH \
                                      --img_path $GOOD_IMG


echo "### 5. SPLIT TRAIN TEST ###"
python3 src/split_train_test.py --label_txt $NEW_LABEL_PATH

echo "### 6. MOVE  FILE"
TRAIN_IMG=$ROOT/train
VAL_IMG=$ROOT/val
TEST_IMG=$ROOT/test

mkdir -p $TRAIN_IMG
mkdir -p $VAL_IMG
mkdir -p $TEST_IMG

TRAIN_LABEL=$ROOT/train.txt
VAL_LABEL=$ROOT/val.txt
TEST_LABEL=$ROOT/test.txt

echo "### 6.1 MOVE TRAIN IMAGES"
python3 src/split_image.py --label_txt $TRAIN_LABEL \
                           --src_img $GOOD_IMG \
                           --tgt_img $TRAIN_IMG


echo "### 6.2 MOVE VAL IMAGES"
python3 src/split_image.py --label_txt $VAL_LABEL \
                           --src_img $GOOD_IMG \
                           --tgt_img $VAL_IMG

echo "### 6.1 MOVE TEST IMAGES"
python3 src/split_image.py --label_txt $TEST_LABEL \
                           --src_img $GOOD_IMG \
                           --tgt_img $TEST_IMG

echo "### 7. ZIP FILE"
python3 src/zip_file.py --root $ROOT
