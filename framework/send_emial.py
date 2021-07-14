#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : send_emial.py
# @Author: gushui
# @Date  : 2021/7/1
# @Desc  :
# ！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
# @Time : 2020/10/26 20:32
# @File  : handle_email.py
# @Author: adeng
# @Date  : 2020/10/26
============================
"""

from datetime import datetime
import os
import yaml
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


# from scripts.handle_file import HandleFile
# from Common.constants import ALLURE_REPORTS_DIR, EMAIL_CONF_FILE_PATH

# import yagmail
# # 使用的账号服务器
# yag=yagmail.SMTP(user='duolaameng250@163.com',
#                  password='GHUXCKZOKFFFHQYV',
#                     host='smtp.163.com')
# # 发送的正文
# contt = ['hello,xiaoxiaobai',''''I'm solid-water ''',yagmail.inline(r'E:\project\find1\aaa\中国钱币博物馆\1.jpg')]

# 发送，收件人，主题，附件
# 收件人可以用列表抱着，可以一次发送给多个 附件也可以
# yag.send('2770488802@qq.com','HI',contt)
# 断开连接
# yag.close()

class HandleEmail():

    def __init__(self, *args, **kwargs):
        # ------加载conf/emailconf.yaml 数据----
        dir = os.path.dirname(os.path.abspath('.'))
        with open(rf'{dir}\data\email.yaml', "r") as f:
            # datas = yaml.load(f, Loader=yaml.FullLoader)  # Loader=yaml.FullLoader 去除警告
            datas = yaml.safe_load(f)
        try:
            self.host = datas["send_email"]['smtp']['host']
            self.port = datas["send_email"]['smtp']['port']
            self.email = datas["send_email"]['email']
            self.pwd = datas["send_email"]['pwd']
            self.receiver = datas["receiver"]
            self.sender = datas["send_email"]['sender']
        except Exception as err:
            print("ERROR：\n" + str(err) + "\n")
            print(f"请检查是否有将send_email添加到emailconf配置文件里")

    # 添加文本
    def add_text(self, text):
        return MIMEText(text, "plain", "utf-8")

    # 添加html文本
    def add_html_text(self, html):
        return MIMEText(html, "html", "utf-8")

    # 添加附件,图片，txt,pdf,zip
    def add_accessory(self, filepath):
        with open(rf'{filepath}', 'rb') as f:
            r = f.read()
        res = MIMEText(f"{r}", "base64", "utf-8")
        res.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filepath))
        return res
        # 添加主题 发件人，收件人

    def add_subject_attach(self, send_email, receiver, subject, sender, attach_info: tuple, send_date=None):
        """
        @param send_email: 发送方email
        @param receiver:  接收方email群发是列表形式 ["xxx@qq.com",XXXX@qq.com,....]
        @param subject: 邮件主题
        @param sender: 发送发的名字，一般指测试人员
        @param attach_info: 构建附件元组
        @param send_date: 发送日期，"%Y-%m-%d %H:%M:%S"，当为None时用当前时间发送邮件
        @return: msg 可以传给 send_email(）方法发送邮件
        """

        msg = MIMEMultipart('mixed')
        msg['Subject'] = subject
        # msg['From'] = '{0} <{1}>'.format(datas["send_email"][send_email][0], send_email)
        msg['From'] = '{0}<{1}>'.format(sender, send_email)
        msg['To'] = ";".join(receiver)

        # print(msg['from'])
        # input()

        # message['From'] = "wumian<**********@163.com>"
        # message['To'] = "qishi<**********@qq.com>"
        if send_date:
            msg['Date'] = send_date
        else:
            msg['Date'] = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        if isinstance(attach_info, tuple):
            for i in attach_info:
                msg.attach(i)
        return msg

    def send_email(self, send_email, pwd, receiver, msg):

        try:
            smtp = smtplib.SMTP(self.host, port=self.port)
            smtp.login(send_email, pwd)
            smtp.sendmail(send_email, receiver, msg.as_string())
            print("{0}给{1}发送邮件成功,发送时间:{2}".format(send_email, receiver,
                                                  datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")))
            smtp.quit()
        except Exception as e:
            print('SMTP Exception:\n' + str(e) + '\n')
            raise e

    def send_allure_email(self, send_email, subject, report_name, send_date=None,
                          text="本邮件由系统自动发出，无需回复！\n各位同事，大家好，以下为本次测试报告."):
        """
        此方法是为公司定制发送Outputs/allure_reports的测试报告打包 群发到邮件
        数据读写的是configs/emailcof.yaml中的数据
        @param send_email: 发送方的邮件
        @param subject:  主题 格式字符串
        @param report_name: 测试报告名字  字符串
        @param send_date: 日期 字符串 %Y-%m-%d %H:%M:%S
        @param text: 正文文本
        @return: None
        """
        # 添加文本内容
        pwd = self.pwd
        receiver = self.receiver
        sender = self.sender
        text = text
        text_plain = self.add_text(text)
        # 先将ALLURE_REPORTS_DIR打包成zip再发送附件
        t = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S_")
        file_package_path = os.path.join(ALLURE_REPORTS_DIR, f"{t}{report_name}")
        allure_report = HandleFile.make_package(file_package_path, "zip", ALLURE_REPORTS_DIR)
        # 添加附件
        zip_allure = self.add_accessory(allure_report)
        # 构建附件元组
        attach_info = (text_plain, zip_allure)

        # 添加主题,附件信息 添加到msg
        msg = self.add_subject_attach(send_email, receiver, subject, sender, attach_info=attach_info,
                                      send_date=send_date)
        # 发送邮件
        self.send_email(send_email, pwd, receiver, msg)

    def send_public_email(self, subject, text,send_date=None,  hmtl='',
                          filepath=None):

        print(text)

        attach_info = []
        text_plain = self.add_text(text=text)
        attach_info.append(text_plain)
        if hmtl:
            text_html = self.add_html_text(html=hmtl)
            attach_info.append(text_html)
        elif filepath:
            file_attach = self.add_accessory(filepath=filepath)
            attach_info.append(file_attach)
        # 构建附件元组
        attach_info = tuple(attach_info)
        # 添加主题和附件信息到msg

        # # print(self.pwd)
        # print(type(self.pwd))
        # # input()
        msg = self.add_subject_attach(send_email=self.email, receiver=self.receiver, subject=subject,
                                      sender=self.sender, attach_info=attach_info, send_date=send_date)
        # 发送邮件
        self.send_email(send_email=self.email, pwd=self.pwd, receiver=self.receiver, msg=msg)


# if __name__ == '__main__':
#     # HandleEmail().send_allure_email("17740xxxx@qq.com", "这是一封全国最帅男人的告白", "allure_测试报告")
#     send_email = "duolaameng250@163.com"
#     receiver = ['duolaameng250@163.com','guwater@126.com','yuxinxi0815@gmail.com']
#     pwd = "GHUXCKZOKFFFHQYV"
#     sender = "yuxinxi"
#     subject = "善良哥哥就是帅"
#     text = "我就是那么帅，走到哪里都有风.\n闾阎扑地，钟鸣鼎食之家.\n舸舰弥津，青雀黄龙之舳.\n云销雨霁，彩彻区明。落霞与孤鹜齐飞，秋水共长天一色.\n"
#     # filepath = r"C:\Users\A\Desktop\工作文档\优惠卷代办问题.txt"
#     HandleEmail().send_public_email(send_email, receiver, pwd, sender, subject, send_date=None, text=text,hmtl="")

if __name__ == '__main__':
    subject = "善良哥哥就是帅"
    text = "我就是那么帅，走到哪里都有风.\n闾阎扑地，钟鸣鼎食之家.\n舸舰弥津，青雀黄龙之舳.\n云销雨霁，彩彻区明。落霞与孤鹜齐飞，秋水共长天一色.\n"
    HandleEmail().send_public_email(subject, text)
