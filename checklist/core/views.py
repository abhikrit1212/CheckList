from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import CheckListSerializer,CheckListItemSerializer
from .models import CheckList,CheckListItem
# Create your views here.

class CheckListsAPIView(APIView):
    serializer_class=CheckListSerializer
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        data=CheckList.objects.all()
        serializer=self.serializer_class(data,many=True)
        serialized_data=serializer.data
        return Response(serialized_data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data=serializer.data
            return Response(serialized_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CheckListAPIView(APIView):
    serializer_class=CheckListSerializer
    def get_object(self,pk):
        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        serializer=self.serializer_class(self.get_object(pk))
        serialized_data=serializer.data
        return Response(serialized_data,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        checkList=self.get_object(pk)
        serializer=self.serializer_class(checkList,data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data=serializer.data
            return Response(serialized_data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        checkList=self.get_object(pk)
        checkList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CheckListItemCreateAPIView(APIView):
    serializer_class=CheckListItemSerializer
    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data=serializer.data
            return Response(serialized_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CheckListItemAPIView(APIView):
    serializer_class=CheckListItemSerializer
    def get_object(self,pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckListItem.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        checklist_item=self.get_object(pk)
        serializer=self.serializer_class(checklist_item)
        serialized_data=serializer.data
        return Response(serialized_data,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        checklist_item=self.get_object(pk)
        serializer=self.serializer_class(checklist_item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data=serializer.data
            return Response(serialized_data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        checklist_item=self.get_object(pk)
        checklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    








        



