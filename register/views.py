from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Waitlist
from .serializers import WaitlistSerializer
# from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# from django.contrib.auth import authenticate
# from django.forms import model_to_dict
from rest_framework.exceptions import ValidationError,PermissionDenied
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token

@swagger_auto_schema(method='post', 
                    request_body=WaitlistSerializer())
@api_view(['POST'])
def waitlist(request):

    if request.method == 'POST':

        serializer = WaitlistSerializer(data=request.data)

        if serializer.is_valid(): #validate the data that was passed
            serializer.save()
            data = {
                'message' : 'success',
                'data'  : serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
        else:
            data = {
                'message' : 'failed',
                'error'  : serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
