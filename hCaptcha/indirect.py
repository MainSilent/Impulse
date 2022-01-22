import os
import time
import json
import gzip
from seleniumwire.webdriver import ChromeOptions
from seleniumwire.undetected_chromedriver import Chrome

key = ""
host = ""
driver = None

def request_interceptor(request):
	if "https://hcaptcha.com/checksiteconfig" in request.url:
		request.url = f"https://hcaptcha.com/checksiteconfig?host={host}&sitekey=f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34&sc=1&swa=1"
	elif "https://hcaptcha.com/getcaptcha" in request.url:
		modify = request.body.decode('utf-8').split("&")
		modify[2] = f"host={host}" 
		request.body = bytes("&".join(modify), 'utf-8')
		del request.headers['Content-Length']
		request.headers['Content-Length'] = str(len(request.body))

def response_interceptor(request, response):
	if "https://hcaptcha.com/getcaptcha" in request.url:
		global key
		body = gzip.decompress(response.body).decode('utf-8')
		data = json.loads(body)
		try:
			if data["bypass-message"]:
				key = False
		except:
			key = data['generated_pass_UUID']
		driver.close()

def new(_host, sitekey, chromedriver_path="/bin/chromedriver", headless=True):
	global driver
	host = _host

	if not os.path.exists(chromedriver_path):
		raise Exception("Chromedriver not found")

	options = ChromeOptions()
	options.add_argument("--headless") if headless else None
	driver = Chrome(executable_path=chromedriver_path, options=options)
	driver.request_interceptor = request_interceptor
	driver.response_interceptor = response_interceptor
	print("Loading page...")

	page_content = f'''
		<script src="https://hcaptcha.com/1/api.js" async defer></script>
		<div class="h-captcha" data-sitekey="{sitekey}"></div>
	'''
	driver.get(f"data:text/html;charset=utf-8,{page_content}")

	print("Waiting for checkbox...")
	while True:
		try:
			driver.switch_to.frame(0)
			driver.find_element_by_id("checkbox").click()
			print("Checkbox clicked")
			break
		except Exception as e:
			driver.switch_to.default_content()
			time.sleep(0.2)

	print("Waiting for key...")
	while True:
		if key != "":
			return key
		time.sleep(0.2)

