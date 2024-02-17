# source 
##############
### CHANGE ###
##############

LABEL_PATH='xi_mang_go/xi_mang/Label.txt'
NEW_LABEL_PATH='xi_mang_go/labeled/xi_mang/1k/Label_100.txt'
IMG_PATH='xi_mang_go/labeled/xi_mang/1k/img'
START=1
END=100

##################
### END CHANGE ###
##################

echo "###0. Preprocess"
# Not IMG_PATH


echo "### 1. GET LABEL ###"
python3 src/get_label.py --label_txt $LABEL_PATH \
                         --new_label_txt $NEW_LABEL_PATH \
                         --start $START \
                         --end $END

echo "### 2. FILTER IMAGE ###"


echo "### 3. REMOVE DUPLICATE IMAGE ###"

echo "### 4. MATCH IMAGE WITH LABEL ###"

echo "### 5. SPLIT TRAIN TEST ###"

echo "### 6. ZIP FILE"
