from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from .models import Waitlist
from django.core.mail import send_mail



@receiver(post_save,sender=Waitlist)
def welcome_mail(sender, instance, created, *args,**kwargs):

    if created:
        
        message= f"""Welcome {instance.first_name}!
# You have successfully registered on our platform! 
# Regards,
# IVATECH"""
        send_mail(
            subject="WAITLIST",
            message=message,
            from_email="ikechukwuklinsman@gmail.com",
            recipient_list=[instance.email]
        )  

