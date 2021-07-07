#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :baidu_test.py.py
# @Time      :2021/1/29 18:02
# @Author    :shui
# coding=utf-8
import os
import time
# import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from framework.base_page import BasePage,Del
import pytest
import allure



# @allure.feature('旎浩')
@allure.epic("项目名称: 旎浩")
@allure.feature("订单模块")
class Test_BaiduSearch(object):

    def setup_class(self):
        self.d=Del()
        a = ['temp', 'report','screenshots']
        self.d.del_mulu(a[0])
        self.d.del_mulu(a[1])
        self.d.del_mulu(a[2])

    def setup(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine()
        self.driver = browse.open_browser(self)


    def teardown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()


    @allure.title('订单流程')
    def test_nhshangcheng(self):
        #  优化建议：设置购物数量，页面跳转时间，增加报错说明，优化查找元素，优化报错后的处理方式，设置截图，参考博客说明优化框架，可以加入数据库来对比操作步骤有没有错误

        test = BasePage(self.driver)
        test.wait(15)  # 隐性等待20s

        # 进入主页
        try:
            test.click('xpath=>//*[@id="details-button"]')
        except:
            pass
        try:
            test.click('xpath=>//*[@id="proceed-link"]')
        except:
            pass

        # 登录
        test.move_to_element('xpath=>/html/body/div[1]/div/ul/li[3]/div/span')
        test.get_windows_img('首页截图')
        test.click('xpath=>/html/body/div[1]/div/ul/li[3]/div/span')
        test.click('xpath=>/html/body/div[1]/div/ul/li[3]/div/div/a[3]')
        time.sleep(2)
        test.send_keys('xpath=>//*[@id="email"]', '2770488802@qq.com')
        time.sleep(2)
        test.send_keys('xpath=>//*[@id="password"]', '123456')
        time.sleep(2)
        test.click('id=>saveButton')

        # 搜索花
        test.send_keys('xpath=>//*[@id="querya"]', 'flower earrings')

        # 点击enter
        test.enter()
        time.sleep(3)

        test.move_to_element('xpath=>//*[@id="J_Goods_List"]/div[1]/a/div[1]/img')
        test.click('xpath=>//*[@id="J_Goods_List"]/div[1]/div')

        # 选择购物数量
        # al=dr.switch_to.alert
        test.click('xpath=>//*[@id="J_Card_Modal"]/div[1]/div[2]/div[3]/div/div/table/tbody/tr[1]/td[4]/div/input[3]')
        test.click('xpath=>//*[@id="AddToCart"]')
        time.sleep(2)
        test.click('class_name=>cart')
        time.sleep(1)
        test.click("class_name=>checkout-btn")

        # 点击立即支付
        time.sleep(3)
        test.click('class_name=>now-btn')
        test.move_to_element('xpath=>//*[@id="payJump"]')
        test.click('xpath=>//*[@id="payJump"]')

        # try:
        #     test.find_element('link_text=>502 Bad Gateway')
        #     test.back()
        #     time.sleep(5)
        #     test.forward()
        # except:
        #     pass

        # 付款界面
        # 进入框架
        test.switch_to_frame('xpath=>//*[@id="injectedUnifiedLogin"]/iframe')
        test.send_keys('xpath=>//*[@id="email"]','sb-k423u3452180@business.example.com')
        test.send_keys('xpath=>//*[@id="password"]','T>MnLvZ6')

        test.click('xpath=>//*[@id="btnLogin"]')
        # 退出框架
        test.switch_to_default_content()


        time.sleep(10)
        while True:
            try:
                test.click('xpath=>//*[@id="confirmButtonTop"]')
                break
            except:
                pass
        test.get_windows_img('完成截图')

        time.sleep(10)
        # 退出
        test.close()


@allure.feature("测试模块")
class Test_login(object):
    def test02(self):
        pass


if __name__ == '__main__':
    pytest.main(['-s', 'test_nh.py', '--alluredir', '../temp'])
    dir = os.path.dirname(os.path.abspath('.'))
    allure_path = dir + r'\tools\allure-2.13.8\bin\allure.bat'
    # print(allure_path)
    os.system(fr'{allure_path} generate ../temp -o ../report --clean')



'''
基本流程跑完了，可以pass   但是有些问题
1，比如点击的操作，有些按钮是不显示的，只有当按钮放到上边时才可以发现点击，目前不知道如何处置
2，没有采用数据驱动，未编写yaml文件
3，必须有python模块可用，移植性不好
4，对于异常的处理没有搞定，稳定性差
5，编码格式问题，log的编码会报错，不知如何解决，在cmd进行allure时也会保编码格式的错
6，allure需要Java环境
7，对于延迟的把控不好，有些页面会有东西遮挡元素，当操作过快时会出现点击了但是没反映情况目前使用延迟来处理，留待后续处理
'''