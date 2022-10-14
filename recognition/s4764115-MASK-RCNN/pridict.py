## Pridiction of the Mask R-CNN 

import numpy as np
import datetime
import skimage

from mrcnn.model import load_image_gt
from mrcnn.model import mold_image
from mrcnn.utils import compute_ap
from mrcnn.config import Config
from mrcnn.visualize import display_instances, display_top_masks
from numpy import expand_dims
from numpy import mean
from matplotlib.patches import Rectangle
from train import Trained_model
from dataset import train
from matplotlib import pyplot as plt
from modules import PredictionConfig, evaluate_model
 

# evaluate model on training dataset
cfg = PredictionConfig()
model = Trained_model(mode='inference', model_dir='logs', config=cfg)
model.load_weights('logs/mask_rcnn_marble_cfg_coco_0003.h5', by_name=True, exclude=['mrcnn_class_logits', 'mrcnn_bbox_fc', 'mrcnn_bbox', 'mrcnn_mask'])
train_mAP = evaluate_model(train, model, cfg)
print("Train mAP: %.3f" % train_mAP)

#Test on a single image
test_img = skimage.io.imread("/Users/wotah_man/Documents/UQ/Datasets/maskRCNN_Dataset/test/ISIC_0015997.jpg")
plt.imshow(test_img)

detected = model.detect([test_img])
results = detected[0]
class_names = ['BG', 'lesion']
display_instances(test_img, results['rois'], results['masks'], 
                  results['class_ids'], class_names, results['scores'])


                         