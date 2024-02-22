import csv

from django.core.mail import send_mail
from django.shortcuts import render
import urllib.parse
import requests
from django.shortcuts import render
from django.http import HttpResponse

def tiny_url(request):
    # Your logic for the tinyurl view goes here
    return HttpResponse("This is the TinyURL view")

def send_emails(request):
    csv_file_path =r'D:\projects\pythonProject2\djangoproject\ttm\static\mail.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here
            send_mail(
                subject,
                message_body,
                'sahithikodavali5@gmail.com',
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
    return render(request, 'Emails_sent_successfully.html')