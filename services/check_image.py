""" Image Check / Compress Image"""

import re
import os
from PIL import Image

from common.constant import PATH


def check_image(file_type):
    match = re.match("image/*", file_type)
    return match


def compress_image(data):
    with open(PATH.format(data['name']), 'wb+') as file:
        file.write(data['binary'])
        image = Image.open(PATH.format(data['name']))
        new_img = image.resize((128, 128))
        new_img.save(PATH.format(data['name']))

    with open(PATH.format(data['name']), 'rb') as image_file:
        image = image_file.read()
    os.remove(PATH.format(data['name']))
    return image
