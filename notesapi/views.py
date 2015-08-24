from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from  rest_framework import generics, status, permissions
from notesapi.serializers import UserSerializer, NoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from  notesapp.models import Note

class UserViewSet(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer_class = UserSerializer(queryset, many=True)
        return  Response(serializer_class.data)

class UserRegistration(APIView):
     def post(self,request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    #def post(self,request, format=None):
        #serializer = UserSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self,request, format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return  Response(serializer.data)


    def post(self,request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




