#!/usr/bin/env python3
import os, requests
USER = os.getenv('USER')
directory_images = '/home/{}/supplier-data/images/'.format(USER)
url = "http://localhost/upload/"
images_files = os.listdir(directory_images)

for image in images_files:
    if 'jpeg' in image and not image.startswith('.'):
        image_path = directory_images + image
        # upload the jpeg files
        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})