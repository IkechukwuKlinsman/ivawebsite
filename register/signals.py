from pickle import TRUE
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from .models import Waitlist
# from django.contrib.auth import get_user_model
# import random
# from django.utils import timezone
# from django.core.mail import send_mail
# from django.conf import settings


@receiver(post_save,sender=Waitlist)
def send_mail(sender,instance,created,*args,**kwargs):
    if instance.email is created == True :
        
        message= f"""Welcome!
# You have successfully registered on our platform! 
# Regards,
# IVATECH"""
        send_mail(
            subject="WAITLIST",
            message=message,
            from_email="ikechukwuklinsman@gmail.com",
            recipient_list=[instance.email]
        )  

