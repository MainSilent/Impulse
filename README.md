# Captcha Impulse

Bypass hCaptcha with Vision AI using yolov5

```
pip install Captcha-Impulse
```

## Available labels

If the requested label is not in the trained model the library will reload the captcha until it find an available label.

<table>
    <tr>
        <th>Name</th>
        <th>Status</th>
    </tr>
    <tr>
        <td>Airplane</td>
        <td>✅</td>
    </tr>
    <tr>
        <td>Seaplane</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Bus</td>
        <td>✅</td>
    </tr>
    <tr>
        <td>Boat</td>
        <td>✅</td>
    </tr>
    <tr>
        <td>Bridge</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Bicycle</td>
        <td>✅</td>
    </tr>
    <tr>
        <td>Car</td>
        <td>✅</td>
    </tr>
    <tr>
        <td>Chimneys</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Crosswalks</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Fire hydrants</td>
        <td>✅</td>
    </tr>
    <tr>
        <td>Mountain | Hill</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Motorcycle</td>
        <td>✅</td>
    </tr>
    <tr>
        <td>Palm tree</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Stairs</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Taxis</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Train</td>
        <td>✅</td>
    </tr>
    <tr>
        <td>Truck</td>
        <td>✅</td>
    </tr>
    <tr>
        <td>Tractor</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Traffic lights</td>
        <td>✅</td>
    </tr>
</table>

## Example

```python
from impulse import Solver
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://democaptcha.com/demo-form-eng/hcaptcha.html")
    solver = Solver(driver)
    solver.run()
```

## Todo

1- Add ReCaptcha