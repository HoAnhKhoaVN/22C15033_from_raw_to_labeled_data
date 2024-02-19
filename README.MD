# 22C15033 From raw to labeled data

Code to process from raw to labeled data. The output is zip file that can run detection. After receive zip file, I will upload to my drive and run Colab for training text detection

**Table of content:**
1. [Prerequisites](#item-one)
2. [Install](#item-two)
3. [Architechture](#item-three)

<!-- headings -->
<a id="item-one"></a>

## 1. Prerequisites
To run the code, you need to install the following libraries:
- duplicate_images

<a id="item-two"></a>

## 2. Install
- Step 1: Install library
```sh
source <path_to_venv>
pip install -r requirements.txt
```

- Step 2: Copy images from source to images. Change paths in `script/run.sh`

- Step 3: Run code follow commands
```sh

sh script/run.sh
```
**Example**:
```sh
source D:/Master/OCR_Nom/deploy/azure/str_vietnam_temple/.venv/Scripts/activate
pip install -r requirements.txt
sh script/run.sh
```

### Generate fileState.txt for PPOCRLabel
Change code in `src/gen_file_state.py` and run command:
```sh
python3 src/gen_file_state.py
```

<a id ="item-three"></a>

## 3. Architechture
There are 6 stage for this repo:
1. Get label follow by index.
2. Filter image: Split good and bad image. The bad images are no bounding box in Label.txt.
3. Remove duplicate images
4. Match image with label
5. Split train test and validation
6. Zip file

