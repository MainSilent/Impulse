import os
import re
from yolov5 import predict
from confusables import normalize
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

weights_path = os.path.join(os.path.dirname(__file__), "yolov5/yolov5x6.pt")

labels = [
    'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant'
]

class Solver():
    timeout = 10
    driver = None
    
    def __init__(self, driver, _type='recaptcha'):
        self.type = _type
        self.driver = driver

    def run(self):
        if self.type == 'recaptcha':
            self.solve_recaptcha()
        else:
            self.solve_hcaptcha()

    def solve_hcaptcha(self):
        iframe = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.h-captcha iframe'))
        )

        # Click on check box
        self.driver.switch_to.frame(iframe)
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#checkbox'))
        ).click()
        self.driver.switch_to.default_content()

        # Get challenge label
        iframe = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[src *= "hcaptcha-challenge.html"]'))
        )
        self.driver.switch_to.frame(iframe)
        raw_label = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.prompt-text'))
        ).text

        raw_label = normalize(raw_label, prioritize_alpha=True)[0].lower()

        for label in labels:
            if label in raw_label:
                print(label)

    def recaptcha(self):
        ...