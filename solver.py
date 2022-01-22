import os
import re
import time
import logging
from yolov5 import predict
from confusables import normalize
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
weights_path = os.path.join(os.path.dirname(__file__), "yolov5/yolov5x6.pt")

labels = [
    'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant'
]

def direct_prediction(image):
    return predict(weights=weights_path, image=image, only_labels=True)

class Solver():
    label = ''
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
        log.info('Clicking on check box')
        self.driver.switch_to.frame(iframe)
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#checkbox'))
        ).click()
        self.driver.switch_to.default_content()
        log.info('Checkbox clicked')

        # Get challenge label
        log.info('Getting challenge label')
        iframe = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[src *= "hcaptcha-challenge.html"]'))
        )
        self.driver.switch_to.frame(iframe)

        while True:
            raw_label = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.prompt-text'))
            ).text

            raw_label = normalize(raw_label, prioritize_alpha=True)[0].lower()
        
            for label in labels:
                if label in raw_label:
                    self.label = label
                    break
            
            # If the label is not in available classes, reload
            if self.label:
                break
            else:
                WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.refresh.button'))
                ).click()
                time.sleep(2)
        log.info('Challenge label: ' + self.label)

        # Get Images
        get_src = lambda i: i.value_of_css_property('background-image')[5:-2]

        log.info('Getting images...')
        while True:
            images = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.task-image .image'))
            )
            
            # Wait for all images to be loaded
            loaded = all([
                get_src(image) for image in images
            ])
            
            if not loaded:
                continue

            # Predict images
            for index, image in enumerate(images):
                src = get_src(image)
                result = direct_prediction(src)

                if self.label in result:
                    self.driver.execute_script(f"document.querySelectorAll('.task-image .image')[{index}].click()")
                    print(f'Image {index+1} Result: {str(result)} Status: True')
                else:
                    print(f'Image {index+1} Result: {str(result)} Status: False')

            self.driver.find_element(By.CSS_SELECTOR, '.button-submit.button').click()

            # When submitting it stays at the frame and if it has been successful it will continue and cause exception
            time.sleep(4)   

            try:
                if not self.driver.find_element(By.CSS_SELECTOR, '.task-image .image'):
                    self.driver.switch_to.default_content()
                    break
            except:
                self.driver.switch_to.default_content()
                break

    def recaptcha(self):
        ...
