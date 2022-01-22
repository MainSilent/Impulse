import os
import time
import json
import gzip
import logging
from solver import Solver
from seleniumwire.webdriver import ChromeOptions
from seleniumwire.undetected_chromedriver import Chrome

logging.getLogger("seleniumwire").setLevel(logging.CRITICAL)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

key = ""
host = ""
driver = None

urls = {
    'api': "https://hcaptcha.com/1/api.js",
    'config': "https://hcaptcha.com/checksiteconfig",
    'getcaptcha': "https://hcaptcha.com/getcaptcha",
    'checkcaptcha': "https://hcaptcha.com/checkcaptcha"
}

def request_interceptor(request):
    if urls['config'] in request.url:
        request.url = f"{urls['config']}?host={host}&sitekey=f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34&sc=1&swa=1"
    elif urls['getcaptcha'] in request.url:
        modify = request.body.decode('utf-8').split("&")
        modify[2] = f"host={host}" 
        request.body = bytes("&".join(modify), 'utf-8')
        del request.headers['Content-Length']
        request.headers['Content-Length'] = str(len(request.body))
    elif urls['checkcaptcha'] in request.url and request.method == "POST":
        body = request.body.decode('utf-8')
        data = json.loads(body)
        data['serverdomain'] = host
        request.body = json.dumps(data).encode('utf-8')
        del request.headers['Content-Length']
        request.headers['Content-Length'] = str(len(request.body))

def response_interceptor(request, response):
    if urls['getcaptcha'] in request.url or urls['checkcaptcha'] in request.url:
        global key
        body = gzip.decompress(response.body).decode('utf-8')
        data = json.loads(body)
        try:
            if data["bypass-message"]:
                key = "" if urls['getcaptcha'] in request.url else False
        except:
            key = data['generated_pass_UUID']

def new(_host, sitekey, chromedriver_path="/bin/chromedriver", headless=True):
    global driver, host
    host = _host

    if not os.path.exists(chromedriver_path):
        raise Exception("Chromedriver not found")

    options = ChromeOptions()
    options.add_argument("--headless") if headless else None
    driver = Chrome(executable_path=chromedriver_path, options=options)
    driver.request_interceptor = request_interceptor
    driver.response_interceptor = response_interceptor
    log.info("Loading page...")

    page_content = f'''
        <script src="{urls['api']}" async defer></script>
        <div class="h-captcha" data-sitekey="{sitekey}"></div>
    '''
    driver.get(f"data:text/html;charset=utf-8,{page_content}")

    log.info("Waiting for solver...")
    solver = Solver(driver, _type="hcaptcha")
    solver.run()

    log.info("Waiting for key...")
    while True:
        if key != "":
            driver.close()
            return key
        time.sleep(0.2)

