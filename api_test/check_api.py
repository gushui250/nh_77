#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : check_api.py
# @Author: gushui
# @Date  : 2021/8/12
# @Desc  :

import time
import requests
import xlrd


class Api():
    def check_api_false(self, file):
        # 检测api是否有效
        with xlrd.open_workbook(file) as t:
            y = len(t.sheets())
            if 1 <= y:
                sheet = t.sheets()[1 - 1]
                for i in range(sheet.nrows):
                    for i in sheet.row_values(i):
                        url = i
                        try:
                            res = requests.get(url)
                            html_1 = res.status_code
                            if html_1 != 200:
                                time.sleep(0.2)
                        except EnvironmentError as  e:
                            print(f'该链接：{url}，无法访问，错误原因： {e} ')


if __name__ == "__main__":
    Api().check_api_false(r'E:\nh修正版\nh\data\接口文档.xlsx')
