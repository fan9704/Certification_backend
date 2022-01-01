import re
from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from restfulapi import models
from restfulapi.serializers import CertificationSerializer,UserSerializer
from rest_framework import viewsets,status,generics,mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.permissions import IsAuthenticated
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)

@api_view(["GET","POST" ,"PUT","PATCH", "DELETE"])
def certification_api_view(request, pk=None):
    permission_classes = [IsAuthenticated]
    if request.method == "GET":
        if pk==None:
            product = models.certification.objects.all()
        else:
            pk=int(pk)
            product = models.certification.objects.get(pk=pk)
        serializer = CertificationSerializer(product)
        return Response(serializer.data)
    elif request.method=="POST":
        print(request.data)
        name=request.data.get("name",'')
        if name !='' :
            new=models.certification.objects.create(name=name)
            if new:
                print("Create Certification Success")
                return Response({"status": "success","addcertification":True}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "fail","addcertification":False}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"status": "fail","addcertification":False}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        print(request.data)
        id=request.data.get("id")
        certification = models.certification.objects.get(id)
        serializer = CertificationSerializer(certification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PATCH":
        print(request.data)
        id=request.data.get("id")
        certification = models.certification.objects.get(id=id)
        certification.delete()
        return Response({"delete":"success","id":id},status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        print(request.data)
        id=request.data.get("id")
        certification = models.certification.objects.get(id)
        certification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CertificationViewSet(viewsets.ModelViewSet):
    queryset = models.certification.objects.all()
    serializer_class = CertificationSerializer


class CertificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.certification.objects.all().order_by("id")
    serializer_class = CertificationSerializer



class registerAPI(APIView):
    def post(self, request):
        username=request.data.get("username")
        password=request.data.get("password")
        email=request.data.get('email')
        print(username,email,password)
        User.objects.create_user(username,email,password)
        print("success")
        return Response({"status": "success","register":True}, status=status.HTTP_200_OK)

class editprofileAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        username=request.session.get("username",'')
        if(username !=''):
            user=User.objects.get(username)
            if request.data["password"]==user.password:
                print(username,"---","login")
                print("authenticate success!")
                if request.data["password"]!="":
                    password=request.data["password"]
                    user.set_password=password
                if request.data["first_name"]!="":
                    first_name=request.data['first_name']
                    user.first_name = first_name
                if request.data["last_name"]!="":
                    last_name=request.data["last_name"]
                    user.last_name = last_name
                if request.data["email"]!="":
                    email=request.data["email"]
                    user.email=email     
                user.save()
            else:
                print("password incorrect")
            if user:
                return Response({"status": "success","edit":True}, status=status.HTTP_200_OK)
        else:
            #status=status.HTTP_400_BAD_REQUEST
            return Response({"status": "error","edit":False,"error":"You haven,t Login"}, status=status.HTTP_200_OK)
    def get(self,request):
        print(request.session.items())
        user_id=request.session.get("_auth_user_id",'')
        if user_id=='':
            return Response({"info":False}, status=status.HTTP_204_NO_CONTENT)
        else:
            user_id=int(user_id)
        user=User.objects.get(id=user_id)
        print(user)
        return Response({"username":user.username,"email":user.email,"first_name":user.first_name,"last_name":user.last_name}, status=status.HTTP_200_OK)
        
class loginAPI(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        print(request.session.items())
        if "_auth_user_id" in request.session:
            print( request.session.get("_auth_user_id",''))
            print("has login")
            print("user?",request)
        else:
            try:
                username=request.data.get("username",'')
                password=request.data.get("password",'')
                print("username",username,"password",password)
                try:
                    user=auth.authenticate(username=username,password=password)
                except:
                    user=None
                if user :
                        auth.login(request, user)
                        request.session["login"]=True
                        request.session["username"]=username
                        print(request.session.items())
                        return Response({"status": "success","login":True}, status=status.HTTP_200_OK)
                else:
                    Response({"status": "success","login":False,"error":"Account or Password Error"}, status=status.HTTP_200_OK)
            except:
                return Response({"status": "error","login":False,"error":"Account or Password Error"}, status=status.HTTP_200_OK)
        return Response({"status": "success","login":True}, status=status.HTTP_200_OK)
            
    def get(self,request):
        user=request.user
        print(user)
        print(request.session.items())
        if user:
            print(user,"logout")
            if 'login' in request.session and 'username' in request.session:
                del request.session['login']
                del request.session['username']
            auth.logout(request)
            return Response({"status": "success","logout":True}, status=status.HTTP_200_OK)
        return Response({"status": "success","logout":False}, status=status.HTTP_200_OK)

