""" Store File"""
from common.constant import PATH

def store_file(data):
    with open(PATH.format(data['name']),'wb') as file:
        file.write(data['binary'])

