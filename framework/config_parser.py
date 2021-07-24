#encoding=utf-8
from configparser import ConfigParser as conf
import os

cur_path=os.path.dirname(os.path.dirname(__file__))
def config(path):
    config=conf()
    absolute_path=cur_path+path
    config.read(absolute_path,encoding='utf-8')
    return config






if __name__ =='__main__':
    path='/config/config.ini'
    config=config(path)
    a=config['testServer']['URL']
    b=config['smtp']['receiver']
    print(b)
    print(type(b))




