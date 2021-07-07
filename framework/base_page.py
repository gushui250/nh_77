#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :base_page.py.py
# @Time      :2021/1/29 17:58
# @Author    :shui

import logging
import os.path
import random
import time
# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from framework.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import allure

logger = Logger()
from selenium import webdriver

from framework.browser_engine import BrowserEngine


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self):

        from selenium import webdriver
        # self.option = webdriver.ChromeOptions()
        # self.option.add_argument(
        #     rf'--user-data-dir=C:\Users\A\AppData\Local\Google\Chrome\UserData\Default')  # 设置成用户自己的数据目录
        # self.option.add_argument(
        #     rf'--user-data-dir=C:\Users\ASUS\AppData\Local\Google\Chrome\UserData\Default')  # 设置成用户自己的数据目录
        #
        dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
        self.chrome_driver_path = dir + '/tools/chromedriver.exe'
        ie_driver_path = dir + '/tools/IEDriverServer.exe'
        self.num = 1  # 计数器

        # self.driver = webdriver.Chrome(chrome_driver_path, options=option)

    # quit browser and end testing
    # read the browser type from config.ini file, return the driver

    def open_browser(self, url):
        self.driver = webdriver.Chrome(self.chrome_driver_path)
        # url="https://www.nhtest.com/"
        # url=rf"{url}"
        # self.driver.delete_all_cookies()
        self.driver.get(url)
        logger.info("Open url: %s" % url)
        self.driver.maximize_window()
        logger.info("Maximize the current window.")
        self.driver.implicitly_wait(10)
        self.get_windows_img('截图')
        logger.info("Set implicitly wait 10 seconds.")
        # return self.driver

    # 打开链接
    def open_url(self, url):

        js = f"window.open('{url}');"  # 新窗口打开链接
        self.driver.execute_script(js)
        toHandle = self.driver.window_handles
        self.driver.switch_to.window(toHandle[-1])

        # #获取当前页面的句柄
        # print(dr.current_window_handle)

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 保存图片
    def get_windows_img(self, IMG):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '\screenshots\\'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : \screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img(IMG)
        with open(f'{screen_name}', 'rb') as f:
            file = f.read()
        allure.attach(file, IMG, allure.attachment_type.PNG)  # 截图到测试报告中

    # 定位元素方法
    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img('错误截图')  # take screenshot

        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':

            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info(f"Had find the element {selector_value} successful ")
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img('错误截图')

        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)

        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    #   输入
    def send_keys(self, selector, text=None):
        try:
            if text.endswith('\n'):
                text = text.replace('\n', '')
        except:
            if text == None:
                text = random.randint(1, 9999)

        try:
            el = self.find_element(selector)
            el.clear()
            el.send_keys(text)
            self.get_windows_img('截图')
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img('错误截图')

    # 清除文本框
    def clear(self, selector):

        try:
            el = self.find_element(selector)
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img('错误截图')


    # 点击元素
    def click(self, selector):

        # self.get_windows_img('截图')
        try:
            el = self.find_element(selector)
            el.click()
            logger.info(f"The element {selector} was clicked.")

        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            # self.get_windows_img('错误截图')
            try:
                self.driver.execute_script('arguments[0].scrollIntoView();', el)
                ActionChains(self.driver).move_to_element(el).click().perform()
            except EnvironmentError as e:
                logger.error(f"Failed to click the element with {e}")
                self.get_windows_img('错误截图')

    #   获取网页标题
    def get_page_title(self):
        logger.info(f"Current page title is {self.driver.title}.")
        return self.driver.title

    # 获取元素内容
    def get_txt(self, selector, txt=None):
        '''
        :param selector:
        :param txt:
        :return:
        '''
        try:
            el = self.find_element(selector)
            dir = os.path.dirname(os.path.abspath("."))
            with open(rf'{dir}\data\{txt}', 'w', encoding='utf-8') as f:
                f.write(el.text)
        except NameError as e:
            logger.error("Failed to get_txt with %s" % e)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

    def move_to_element(self, selector):
        try:
            el = self.find_element(selector)
            ActionChains(self.driver).move_to_element(el).perform()
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img('错误截图')

    def move_to_elements(self, selector, tag):

        selector_value = selector.split('=>')[1]
        dr = self.driver
        el = dr.find_element_by_xpath(selector_value).find_elements_by_tag_name(tag)

        for i in el:
            ActionChains(self.driver).move_to_element(i).perform()
            self.get_windows_img(f'步骤截图{i}')
            time.sleep(2)

    def enter(self):
        try:
            ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
        finally:
            self.get_windows_img('错误截图')

    #   进入框架
    def switch_to_frame(self, selector):
        el = self.find_element(selector)
        self.driver.switch_to.frame(el)

    #   退出框架
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

        # 退出到父框架
        # self.driver.switch_to.parent_frame()


class Del(object):
    def del_99(self, fileDirName):

        '''删除小模块'''
        try:
            file1 = os.listdir(fileDirName)
            for i in file1:
                s = fileDirName + '\\' + i
                dirbool = os.path.isdir(s)
                # 判断是否为目录，返回bool值
                if dirbool == False:
                    fileName = fileDirName + '\\' + i
                    os.remove(fileName)
                elif dirbool == True:
                    fileDir = fileDirName + '\\' + i
                    self.del_99(fileDir)  # 递归 #
                    os.rmdir(fileDir)  # 可以不删除他自身
            # os.removedirs(fileDirName)
            #    os对象的函数递归删除空目录 #
            # print("删除成功！")
        except:
            pass

        # del_99('temp')

    def del_mulu(self, mulu):
        '''
        :param mulu: 输入目录
        :return:
        '''
        dir = os.path.dirname(os.path.abspath('.'))
        fileDirName = dir + '\\' + rf'{mulu}'
        self.del_99(fileDirName)

    # del_fuzhu('temp')


# a = BasePage()
# a.open_browser(rf'https://www.baidu.com')
# # a.sleep(2)
# # a.close()
# # a.sleep(5)
# print(a.get_page_title())
# a.open_url(rf'https://www.nihaojewelry.com')
# # a.click('xpath=>/html/body/div[1]/div/div/a[1]')
# a.get_txt('xpath=>/html/body/div[1]/div/div/a[1]','标题.txt')
# print(a.get_page_title())
# a.open_url(rf'https://www.nihaojewelry.com')
# a.click('xpath=>/html/body/div[1]/div/div/a[1]')
# print(a.get_page_title())