import os
import hashlib
from .yolov5 import predict
from .utils.downloads import safe_download

weights_path = os.path.join(os.path.dirname(__file__), "yolov5x6.pt")
weights_hash = "6ce5c5bc16f21b0d9beef9c2e5d075728f3ed417fc1a76780e4b3e8aff667105"
weights_download_path = "https://github.com/MainSilent/Impulse/releases/download/1.0.0/yolov5x6.pt"

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def download():
    print("After download run the script again")

    safe_download(weights_path,
        url=weights_download_path,
        error_msg=f'\nPlease download the file from {weights_download_path} and move to {weights_path}')

if not os.path.exists(weights_path):
    print("Weights file does not exist")
    input("Press Enter to download: ")
    download()

if os.path.exists(weights_path) and sha256sum(weights_path) != weights_hash:
    print("Weights file is corrupted, The file hash does not match!")
    i = input("Download the file again?[y/N] ")

    if i.lower() == 'y':
        download()