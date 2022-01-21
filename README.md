# Captcha Impulse

Bypass ReCaptcha and hCaptcha with Vision AI using yolov5

## How does it work?

Base on my last research both captchas use 19 classes, By using Vision AI we are able to bypass the captchas with an acceptable probability.

I have plan on training the model on a custom dataset for more labels but this task needs many hours of preprocessing and training, Currently we are using pre trained models.

If the requested label is not in the trained model the library will ReAdd the captcha until it find an available label.

## Available labels

<table>
    <tr>
        <th>Name</th>
        <th>Status</th>
    </tr>
    <tr>
        <td>Airplane | Seaplane</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Bus</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Boat</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Bridge</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Bicycle</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Car</td>
        <td>❌</td>
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
        <td>❌</td>
    </tr>
    <tr>
        <td>Mountain | Hill</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Motorcycle</td>
        <td>❌</td>
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
        <td>❌</td>
    </tr>
    <tr>
        <td>Truck</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Tractor</td>
        <td>❌</td>
    </tr>
    <tr>
        <td>Traffic lights</td>
        <td>❌</td>
    </tr>
</table>