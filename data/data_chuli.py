#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : data_chuli.py
# @Author: gushui
# @Date  : 2021/2/2
# @Desc  :
import csv
import os
import pymysql, xlwt, xlrd

def txt_excel():
    '''
    转换用例工具，还需要修改，目前以一个空格来隔开用例 ，需要改善
    :return:
    '''
    dir = os.path.dirname(os.path.abspath('.'))
    f = open(rf'{dir}\data\a.txt', 'r')
    f1 = f.readlines()
    x = 1
    a = 0

    # print(f1)
    t = xlwt.Workbook(encoding='utf-8')
    sheet = t.add_sheet('phthon1', cell_overwrite_ok=True)
    for i in range(len(f1)):
        print(f1[i])
        if ',' in f1[i]:
            ii = f1[i].split(',')
            for iii in range(len(ii)):
                sheet.write(i - a, iii, ii[iii])
        elif f1[i].startswith('\n'):
            x += 1
            sheet = t.add_sheet(fr'phthon{x}', cell_overwrite_ok=True)
            a = i + 1
        else:
            sheet.write(i - a, 0, f1[i])

    t.save('测试1.xlsx')
    f.close()

class Data_(object):
    def __init__(self):
        self.zzz = [] #一个用例


    # def data01(self):
    #     '''
    #     处理csv文件暂时不用
    #     :return:
    #     '''
    #     a = []
    #     b = {}
    #     c = []
    #     dir = os.path.dirname(os.path.abspath('.'))
    #     with open(fr'{dir}\data\case01.csv', 'r', newline='') as f:
    #         res = csv.reader(f)
    #         r = next(res)
    #         r = next(res)
    #         for i in res:
    #             if i != [] or i != ['结束']:
    #                 a.append(i)
    #     b['tital'] = a  # 添加
    #     c.append(b)


    def data02(self, i):
        '''
        编写用例格式
        :param i:
        :return:
        '''
        z = []
        cc = {}
        zz = []
        dir = os.path.dirname(os.path.abspath(__file__))

        with xlrd.open_workbook(fr'{dir}\测试1.xlsx') as t:
            y = len(t.sheets())
            if i <= y:
                sheet = t.sheets()[i-1]  # 下标位置选择
                for i in range(sheet.nrows):
                    z.append([i for i in sheet.row_values(i) if i != '' and i !='\n'])
                    cc["story"]=z[:1]
                    cc['tital'] = z[2:] # 添加操作步骤
                    # print(cc['tital'])
                    # print(type(cc['tital']))
            if cc["tital"]!=[] and  cc['tital'] is not None:
                zz.append(cc)
            else:
                zz.append(0)
            return zz, y

    def data03(self, *x):
        '''
        用来吧用例传入case,可传入一个，或几个，也可以全传
        :return:zzz
        '''

        if x == ('quanbu',) or x == 'quanbu':
            dir = os.path.dirname(os.path.abspath(__file__))
            with xlrd.open_workbook(fr'{dir}\测试1.xlsx') as t:
                y = [i for i in range(len(t.sheets()))]
                self.data03(y)
        else:
            for i in x:
                if i in [i for i in range(0, 100)]:
                    if self.data02(i)[0] != [0]:
                        self.zzz.append(self.data02(i)[0])
                else:
                    for y in i:
                        if self.data02(y)[0] != [0]:
                            self.zzz.append(self.data02(y)[0])
        return self.zzz

    def story(self,*num):
        story_num = []
        for i in Data_().data03(num):
            story_num.append(i[0]['story'][0][0])
        return story_num[0:]


if __name__ == "__main__":
    try:
        txt_excel()
    except:
        pass
    print(Data_().data03(4,5,6))




# import socket
# s=socket . socket(socket .AF_INET,socket.SOCK_STREAM)
# #生成socket对象
# #获取服务器名称
# host=socket.gethostname()
# #端口号
# port=1234
# #绑定socket地址
# s.bind( (host,port))
# #开始监听
# s.listen(5)
# while True:
#     C, addr = s.accept()
#     # 接受一个连接
#     print(f"连接来自:↓{addr}")
#     C.send('123')
#     # 发送数据
#     C.close()
#     # 关闭连接




#
# import socket
# s=socket. socket (socket .AF_INET, socket . SOCK_STREAM)
# #生成一个Socket对象
# host=socket.gethostname()
# port=1234
# s.connect ( (host,port) )
# #连接服务器
# print(s.recv(1024))
# #读取数据
# s.close ()
# #关闭连接







