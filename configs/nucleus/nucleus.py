_base_ = '../mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'

# change to 1 class 
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)))

dataset_type = 'COCODataset'
classes = ('1',)
data = dict(
    train=dict(
        img_prefix='dataset/',
        classes=classes,
        ann_file='dataset/train.json'),
    val=dict(
        img_prefix='dataset/',
        classes=classes,
        ann_file='dataset/train.json'),
    test=dict(
        img_prefix='dataset/test/',
        classes=classes,
        ann_file='dataset/test_img_ids.json'))

# pre-trained model
load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'