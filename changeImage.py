#!/usr/bin/env python3
from PIL import Image
import sys, os

username = os.getenv('USER') # To get the username from environment variable
directory_images = '/home/{}/supplier-data/images/'.format(username)
for file_image in os.listdir(directory_images):
    if not file_image.startswith('.') and 'tiff' in file_image:
        path_image = directory_images + file_image
        path_file = os.path.splitext(path_image)[0]
        image = Image.open(path_image)
        new_path_file = '{}.jpeg'.format(path_file)
        image.convert('RGB').resize((600, 400)).save(new_path_file, "JPEG")