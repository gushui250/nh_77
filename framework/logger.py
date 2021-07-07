#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :logger.py.py
# @Time      :2021/1/29 18:00
# @Author    :shui
#_*_coding:utf-8 _*_
import logging
import os.path
import time

class Logger(object):
    def __init__(self):
        # '''指定保存日志的文件路径，日志级别以及调用文件将日志存入到指定的文件中'''
        # #创建一个logger
        # self.logger = logging.getLogger(logger)
        # self.logger.setLevel(logging.DEBUG)
        # #创建一个handler，用于写入日志文件
        # rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # log_path = os.path.dirname(os.path.abspath('.'))+'\log\\'
        # #如果case组织结构式/testsuit/fraturemoddel/xxx.py，那么得到的相对路径的父路径就是项目的根目录
        # log_name = log_path + rq + '.log'
        # fh = logging.FileHandler(log_name)
        # fh.setLevel(logging.INFO)
        #
        # #再创建一个handler，用于输出到控制台
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)
        # #定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # fh.setFormatter(formatter)
        # ch.setFormatter(formatter)
        # #给logger添加handler
        # self.logger.addHandler(fh)
        # self.logger.addHandler(ch)

        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')) + '\log\\'
        log_name = log_path + rq + '.log'
        logging.basicConfig(
            filename=f'{log_name}',
            filemode='a',
            format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
            level='INFO'
        )

    #
    # def getlog(self):
    #     return self.logger
    def info(self, param):
        logging.info(f'{param}')

    def error(self, param):
        logging.error(f'{param}')


