import os
from yolov5 import predict

weights_path = os.path.join(os.path.dirname(__file__), "yolov5/yolov5x6.pt")

class Solver():
    driver = None
    
    def __init__(self, driver, _type='recaptcha'):
        self.type = _type
        self.driver = driver

    def run(self):
        if self.type == 'recaptcha':
            solve_recaptcha()
        else:
            solve_hcaptcha()

    def solve_hcaptcha(self):
        print("ok")

    def recaptcha(self):
        ...