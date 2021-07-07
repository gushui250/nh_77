#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :baidu_homepage.py.py
# @Time      :2021/1/29 18:01
# @Author    :shui
# coding=utf-8
from framework.base_page import BasePage


class HomePage(BasePage):
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"

    def type_search(self, text):
        self.send_keys(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

'''
这个模块没啥用，
'''