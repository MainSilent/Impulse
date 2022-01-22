import os
from yolov5 import predict
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

weights_path = os.path.join(os.path.dirname(__file__), "yolov5/yolov5x6.pt")

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

    def recaptcha(self):
        ...