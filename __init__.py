import logging
# import indirect
from yolov5 import predict
from solver import Solver, direct_prediction

logging.disable(logging.CRITICAL)

def set_logging(value=False):
    logging.disable(logging.NOTSET if value else logging.CRITICAL)