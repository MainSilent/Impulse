import logging
from yolov5 import predict

logging.disable(logging.CRITICAL)

def set_logging(value=False):
    logging.disable(logging.NOTSET if value else logging.CRITICAL)

predict(weights="yolov5/yolov5x6.pt", image="")