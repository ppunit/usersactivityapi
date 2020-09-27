from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User,ActivityPeriod
from .serializers import UserDataSerializer

# Create your views here.

class UserList(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserDataSerializer(users,many=True)
        response = {'ok':True,'members':serializer.data}
        return Response(response)
