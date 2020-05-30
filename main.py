import shutil
import requests
import ctypes
import os

url = 'https://unsplash.it/1920/1080/?random'
response = requests.get(url, stream=True)

with open('img.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

abs_path = os.path.abspath("./img.jpg")
print(abs_path)
ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path , 0)
