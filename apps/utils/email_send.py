# -*- coding: utf-8 -*-
from MxOnline.settings import EMAIL_FROM

__author__ = 'ysir'
__date__ = '2018/11/19 10:02 PM'

from random import Random
from users.models import EmailVerifyRecord
from django.core.mail import send_mail


def random_str(randomlength=8):
    str = ''
    chars = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]

    return str


def send_register_email(email, send_type='register'):
    code = random_str(16)
    email_record = EmailVerifyRecord()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '甲乙课堂注册激活链接'
        email_body = '请点击下面的链接激活你的账号： http:127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
