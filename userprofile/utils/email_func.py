# -*- coding: utf-8 -*-
# @Author : Jesse.T
# @Time   : 2019/10/28 13:37
from django.conf import settings
import os 
import uuid
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess

def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()

def send_register_email(address):
    random_str=get_random_str()
    link = settings.DOMAIN+'/userprofile/activate/'+random_str
    title = '[v2et.cn]激活邮箱账号'
    msg=f"""
您好！
<br>
<br>
点击链接即可激活您的v2et.cn账号,
<br>
<br>
{link}
<br>
<br>
为保障您的帐号安全，请在24小时内点击该链接，您也可以将链接复制到浏览器地址栏访问。
<br>
<br>
本邮件由系统自动发出，请勿直接回复！
    """
    subprocess.Popen(['python',os.path.join(os.getcwd(),'userprofile','utils','email_func.py'),
                                     title,msg,address])
    return random_str


def sendmail(subject, msg, toaddrs, fromaddr, smtpaddr, password):
    '''
    @subject:邮件主题
    @msg:邮件内容
    @toaddrs:收信人的邮箱地址
    @fromaddr:发信人的邮箱地址
    @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    @password:发信人的邮箱密码
    '''
    if isinstance(toaddrs,str):
        toaddrs=[toaddrs,]
    mail_msg = MIMEMultipart()
    mail_msg['Subject'] = subject
    mail_msg['From'] = fromaddr
    mail_msg['To'] = ','.join(toaddrs)
    mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))
    try:
        print('准备发送邮件')
        s = smtplib.SMTP_SSL(host=smtpaddr)
        s.connect(smtpaddr, 465)  # 连接smtp服务器
        s.login(fromaddr, password)  # 登录邮箱
        print('登录完成,开始发送')
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string())  # 发送邮件
        s.quit()
        print('发送完成')
    except Exception as  e:
        print(e)

if __name__ == '__main__':
    import sys
    fromaddr = "962080565@qq.com"
    smtpaddr = "smtp.qq.com"
    toaddrs = ["tjx201147@163.com",]
    subject = "最新消息"
    password = "jjkgekpejfckbdee"
    msg = "测试"
    print(sys.argv)
    sendmail(sys.argv[1], sys.argv[2], sys.argv[3], fromaddr, smtpaddr, password)
