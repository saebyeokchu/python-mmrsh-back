from datetime import datetime
import random
from django.core.mail import send_mail

class CustomEmailService :
    def sendAuth(userEmailAddr, randNum) :
        return send_mail(
            subject='[머무름] 머무름 접속 인증번호 입니다',  # Email subject
            message= str(randNum),  # Email body
            from_email='yujin_career@naver.com',  # Sender's email
            recipient_list=[userEmailAddr],  # List of recipients
            fail_silently=False,  # Raise exception if sending fails
        )