# 2021-VRDL-HW3

This repository contains the code for homework 3 of 2021 Fall Selected Topics in Visual Recognition using Deep Learning.

## Installation
```
pip install openmim
mim install mmdet
pip install scikit-image
```

## Data Preparation
1. Download the training set `train.zip`, test set `test.zip`,  and `test_img_ids.json` from [CodaLab](https://codalab.lisn.upsaclay.fr/competitions/333?secret_key=3b31d945-289d-4da6-939d-39435b506ee5#participate-get_data) and put them in `dataset` folder
2. Unzip `train.zip` and `test.zip`
3. Run `python train_preprocessing.py` and `python test_preprocessing.py`

## Quick Start for generating the submitted results
1. Run `mkdir work_dirs`, `cd work_dirs` and `mkdir nucleus` to create folder `work_dirs/nucleus`
2. Download the [model weight](https://drive.google.com/file/d/14n1405ulabjVRhiFUktPmXFMfqG1FWwP/view?usp=sharing) and put `epoch_90.pth` in `./work_dirs/nucleus`
3. Generate the test results
```
python tools/test.py configs/nucleus/nucleus.py  ./work_dirs/nucleus/epoch_90.pth --out ./work_dirs/nucleus/result.pkl --show-dir ./work_dirs/nucleus/test_results
```
4. Run `python ./dataset/test_postprocessing.py` to generate `answer.json` from `result.pkl`

## Train Model
1. Download the pre-trained weight
```
mkdir checkpoints
wget -c https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth \
      -O checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth
```
2. python3 tools/train.py configs/nucleus/nucleus.py


## Acknowledgement
This implementation is heavily based on [MMDetection](https://github.com/open-mmlab/mmdetection).
