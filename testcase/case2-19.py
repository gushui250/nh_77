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

from selenium import webdriver
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


import uiautomator2 as u2




# abd命令大全
# https://www.cnblogs.com/bravesnail/articles/5850335.html
#找到apk，复制到本地
# adb shell pm path com.alibaba.android.rimet  #找到钉钉的包，
# adb pull /data/app/com.alibaba.android.rimet-Gn4orwWR0IKwI8LU-JB6LA==/base.apk C:\Users\A\Downloads\分类页新增

