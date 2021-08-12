#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : case2-19.py
# @Author: gushui
# @Date  : 2021/2/19
# @Desc  :

#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# dr=webdriver.Chrome()
# dr.get('http://www.baidu.com')
# dr.implicitly_wait(20)
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
#
# dr.find_element_by_xpath('//*[@id="kw"]').submit()                 #模拟回车键1
# # dr.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.ENTER)  #模拟回车键2


# coding:utf-8

# from selenium import webdriver
# option = webdriver.ChromeOptions()
# # 假装自己是苹果手机
# option.add_argument('--user-agent=iphone')
#
# # 假装自己是安卓手机
# # option.add_argument('--user-agent=android')
# driver = webdriver.Chrome(options=option)
# driver.get('https://www.nhtest.com/')


#  以 pymysql 为例，实现通过 with 简化数据库操作
# import pymysql
#
#
# class DB():
#     def __init__(self, host='192.168.50.242', port=3306, db='', user='anteater', passwd='Hasdw__01', charset='utf8'):
#         # 建立连接
#         self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
#         # 创建游标，操作设置为字典类型
#         self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
#
#     def sq(self):
#         try:
#             # 执行SQL语句
#             self.cur.execute("SELECT * FROM `test`.`sales_order_dispute` WHERE `order_increment` LIKE '%NHMX21022298404%' ORDER BY `order_increment` DESC LIMIT 0,1000;")
#             # 获取所有记录列表
#             results = self.cur.fetchall()
#             print(results)
#         except:
#             print("Error: unable to fetch data")
#         # 关闭数据库连接
#         self.conn.close()
#
# DB().sq()

# import os
# os.chdir(r'C:\Users\A\Downloads\模拟器净化工具包V1.2\bin')
# # os.system(r'adb shell  am start -n com.alibaba.android.rimet/.biz.LaunchHomeActivity')
# os.system(r'adb shell am start -n com.alibaba.android.rimet/')


# import uiautomator2 as u2


# abd命令大全
# https://www.cnblogs.com/bravesnail/articles/5850335.html
# 找到apk，复制到本地
# adb shell pm path com.alibaba.android.rimet  #找到钉钉的包，
# adb pull /data/app/com.alibaba.android.rimet-Gn4orwWR0IKwI8LU-JB6LA==/base.apk C:\Users\A\Downloads\分类页新增


# from selenium import webdriver
# # # # 假装自己是苹果手机
# # option = webdriver.ChromeOptions()
# # option.add_argument('--user-agent=iphone')
# # 假装自己是安卓手机
# option = webdriver.ChromeOptions()
# option.add_argument('--user-agent=android')
# option.add_argument(rf'--user-data-dir=C:\Users\A\AppData\Local\Google\Chrome\UserData\Default')  # 设置成用户自己的数据目录
# driver = webdriver.Chrome(options=option)
# driver.get('http://192.168.50.37:3021/login')
# driver.set_window_size(400,600)


# import matplotlib.pyplot as plt #导入绘图模块
# from mpl_toolkits.mplot3d import Axes3D #3d绘图模块
# import numpy as np #导入数值计算拓展模块
#
# #start generating points
# x_lim=np.linspace(-10,10,520)
# y_lim=np.linspace(-10,10,520)
# z_lim=np.linspace(-10,10,520)
# X_points=[] #用来存放绘图点X坐标
# Y_points=[] #用来存放绘图点Y坐标
# Z_points=[] #用来存放绘图点Z坐标
# for x in x_lim:
#     for y in y_lim:
#         for z in z_lim:
#             if (x**2+(9/4)*y**2+z**2-1)**3-(9/80)*y**2*z**3-x**2*z**3<=0:
#                 X_points.append(x)
#                 Y_points.append(y)
#                 Z_points.append(z)
#
# ###start plot love
# fig=plt.figure() #画布初始化
# ax=fig.add_subplot(111,projection='3d') #采用3d绘图
# ax.scatter(X_points,Y_points,Z_points,s=20,alpha=0.5,color="red") #3d散点图填充
# plt.show()
#
# import requests
import re
import os
import time

import requests
import xlrd



import xlwt, xlrd


# def data02(self, i=1):
#     '''
#     编写用例格式
#     :param i:
#     :return:
#     '''
#
#     with xlrd.open_workbook(fr"E:\nh修正版\nh\data\444.xlsx‪") as t:
#         y = len(t.sheets())
#         if i <= y:
#             sheet = t.sheets()[i - 1]  # 下标位置选择
#             for i in range(sheet.nrows):
#                 print(i)


#
# data02(1)

# with xlrd.open_workbook(fr"E:\nh修正版\nh\data\444.xlsx‪") as t:
#     y = len(t.sheets())
#     if 1 <= y:
#         sheet = t.sheets()[1 - 1]  # 下标位置选择
#         for i in range(sheet.nrows):
#             print(i)
