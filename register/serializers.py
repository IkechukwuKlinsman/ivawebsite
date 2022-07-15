from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from .models import Waitlist
# from .signals import get_otp
from django.core.mail import send_mail


class WaitlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Waitlist
        fields = '__all__'
