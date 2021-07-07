#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_case01.py
# @Author: gushui
# @Date  : 2021/2/1
# @Desc  :
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# __title__  =
# __Time__   = 2020/10/27 19:44
# __Author__ = 小菠萝测试笔记
# __Blog__   = https://www.cnblogs.com/poloyy/
# """
# import os
# import allure
# import pytest
#
# @pytest.fixture(scope="session")
# def login_fixture():
#     print("=== 前置登录 ===")
#
# @allure.step("步骤1")
# def step_1():
#     print("操作步骤---------------1")
#
#
# @allure.step("步骤2")
# def step_2():
#     print("操作步骤---------------2")
#
#
# @allure.step("步骤3")
# def step_3():
#     print("操作步骤---------------3")
#
#
# @allure.epic("epic 相当于总体描述")
# @allure.feature("测试模块")
# class Test_AllureALL(object):
#
#     @allure.testcase("https://www.cnblogs.com/poloyy/", '测试用例,点我一下')
#     @allure.issue("https://www.cnblogs.com/poloyy/p/12219145.html", 'Bug 链接,点我一下')
#     @allure.title("用例的标题")
#     @allure.story("story one")
#     @allure.severity("critical")
#     def test_case_1(self, login_fixture):
#         """
#         小菠萝测试笔记地址：https://www.cnblogs.com/poloyy/
#         """
#         print("测试用例1")
#         step_1()
#         step_2()
#
#     @allure.story("story two")
#     def test_case_2(self, login_fixture):
#         print("测试用例2")
#         step_1()
#         step_3()
#
#
# @allure.epic("另一个 epic")
# @allure.feature("查找模块")
# class Test_AllureALL2(object):
#     @allure.story("story three")
#     def test_case_3(self, login_fixture):
#         print("测试用例3")
#         step_1()
#
#     @allure.story("story four")
#     def test_case_4(self, login_fixture):
#         print("测试用例4")
#         step_3()
#
#
# if __name__ == '__main__':
#     pytest.main(['-s','test_case01.py',  '--alluredir', './allure'])
#     os.system('allure generate ./allure -o ./report --clean')

# coding=utf-8
# import os
#
# import pytest
# import allure
#
# marketid = ['101','102']
# testlist = ['1','test','test1']
# testlist2 = ['test0','test2','test3']
#
# #市场id对应也生成相同的数组
#
# @pytest.fixture(scope='module',autouse=True)
# @allure.feature('测试准备')
# @allure.title('标题')
# def prepare():
#     print('这是测试准备哦')
#     yield
#     print('module 测试结束')
#
# @allure.feature('期权强平测试')
# class Test_module1:
#     @allure.feature('期权市价委托强平')
#     @pytest.mark.parametrize('str1',testlist)
#     @pytest.mark.parametrize('str2',testlist2)
#     def test1(self,str1,str2):
#         """
#             用例描述：期权强平市价委托
#         """
#         stradd = str1 + str2
#         print('这是test1')
#         assert 1 == 2
#
#     @allure.feature('期权限价委托强平')
#     def test2(self):
#         with allure.step("调节持仓"):
#             x = '1'
#             allure.attach(x)
#             print('这是test2')
#         with allure.step('进行强平的操作'):
#             print('DTE')
#
# class Test_module2:#在这里插入代码片`
#     def test3(self):
#         with allure.step("调节持仓"):
#             x = '1'
#             allure.attach(x)
#             print('这是test2')
#         with allure.step('进行强平的操作'):
#             print('DTE')
# if __name__ == '__main__':
#     pytest.main(['-s','test_case01.py',  '--alluredir', './allure'])
#     os.system('allure generate ./allure -o ./report --clean')


# 关键字驱动


import os
import time
# import unittest
# from framework.browser_engine import BrowserEngine
# from pageobjects.baidu_homepage import HomePage
from framework.base_page import BasePage, Del
import pytest
import allure
from data.data_chuli import Data_




# @allure.feature('旎浩')
@allure.epic("项目名称: 旎浩")
class Test_BaiduSearch(object):

    def setup_class(self):
        self.driver = BasePage()
        self.d = Del()
        a = ['temp', 'screenshots']
        for i in a:
            self.d.del_mulu(i)


    # def setup(self):
    #     """
    #     测试固件的setUp()的代码，主要是测试的前提准备工作
    #     :return:
    #     """
    # browse = BrowserEngine()
    #     self.driver = browse.open_browser('https://www.nhtest.com/')

    def teardown(self):
        self.driver.close()


    def teardown_class(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit_browser()


    # @allure.story(Data_().data03(4, 5, 6)[story_num][0:]['story'])
    @pytest.mark.parametrize('params', list(Data_().data03(4, 5, 6)),ids=Data_().story(4,5,6))
    def test01(self, params):
        '''
        登录case用例
        :param params:
        :return:
        '''
        params = params[0]['tital']
        print(params)
        for i in params:
            if i != None:
                with allure.step(i[0]):
                    func = getattr(self.driver, i[1])
                    cases = [i for i in list(i[2:]) if i != '' and i != '\n']
                    print(cases)
                    func(*cases)
                    time.sleep(3)



if __name__ == '__main__':
    pytest.main(['-s', 'test_case01.py', '--alluredir', '../temp'])
    dir = os.path.dirname(os.path.abspath('.'))
    allure_path = dir + r'\tools\allure-2.13.8\bin\allure.bat'
    # print(allure_path)
    rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    os.system(fr'{allure_path} generate ../temp -o ../report/html_{rq} --clean')
