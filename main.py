import os
import logging
from yolov5 import predict

logging.disable(logging.CRITICAL)

weights_path = os.path.join(os.path.dirname(__file__), "yolov5/yolov5x6.pt")

def set_logging(value=False):
    logging.disable(logging.NOTSET if value else logging.CRITICAL)

def direct_prediction(image):
    return predict(weights=weights_path, image=image, only_labels=True)