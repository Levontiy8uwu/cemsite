from django.shortcuts import render
from pyrogram import Client
from decouple import config

import smtplib
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "static/main_tab.html")
    if request.method=="POST":
        data = request.POST
        user_name = data["user"]
        phone = data["phone"]
        send(user_name, phone)
        return render(request, "static/main_tab.html")

def send(user_name, phone):
    email = "lev-boyarincev49@yandex.ru"
    password = "tgwfauxguvqttaup"
    dest_email = "pavel-boyarincev@yandex.ru"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Новая заявка" 
    msg['From'] = email
    msg['To'] = dest_email

    html = f"{user_name}, {phone}"

    part2 = MIMEText(html, 'html')

    msg.attach(part2)


    mail = smtplib.SMTP('smtp.yandex.ru')

    mail.ehlo()

    mail.starttls()

    mail.login(email, password)
    mail.sendmail(email, dest_email, msg.as_string())
    mail.quit()
    return 0