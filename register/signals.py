from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from .models import Waitlist
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from django.template import loader
from django.core.mail import EmailMessage
from django.conf import settings


@receiver(post_save,sender=Waitlist)
def welcome_mail(sender, instance, created,**kwargs):
    html_message = loader.render_to_string('C:/Users/Admin/Desktop/IvaWebsite/ivawebsite/templates/email_templates/index.html')
    if instance.email: 


        message= 'WELCOME!!!'
#         f"""Welcome!
# You have successfully registered on our platform! 
# Regards,
# IVATECH"""
        send_mail(
            subject="WELCOME TO IVA!!!",
            message= message,
            from_email="ikechukwuklinsman@gmail.com",
            recipient_list=[instance.email],
            fail_silently= True,
            html_message=html_message
        )  

