#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : a.py.py
# @Author: gushui
# @Date  : 2021/3/1
# @Desc  :


import os
import pytest

dir = os.path.dirname(os.path.abspath('.'))
allure_path = dir + r'\tools\allure-2.13.8\bin\allure.bat'


os.chdir(rf'{dir}\testcase')

pytest.main(['-s', 'test_case01.py', '--alluredir', '../temp'])
# print(allure_path)
os.system(fr'{allure_path} generate ../temp -o ../report --clean')

