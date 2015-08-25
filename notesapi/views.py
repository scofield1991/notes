from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from  rest_framework import generics, status, permissions
from notesapi.serializers import UserSerializer, NoteSerializer, UserProfileSerializer, NoteListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from  notesapp.models import Note
from django.http import  Http404

class UserViewSet(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer_class = UserSerializer(queryset, many=True)
        return  Response(serializer_class.data)

class UserRegistration(APIView):
    """
    To create new user provide next data in json format: "first_name", "last_name","username", "password","email", "birthday": "phone_number"
    """
    def post(self,request, format=None):
        serializer = UserSerializer(data=request.data)
        serializer1 = UserProfileSerializer(data=request.data)

        #user.groups = serialized.init_data['groups']
        print(serializer1.initial_data)
        if   serializer.is_valid() and serializer1.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            profile=serializer1.save(user=user)
            #profile.user = user
            #profile.save()

            return Response([serializer.data, serializer1.data], status=status.HTTP_201_CREATED)
        return  Response([serializer.errors, serializer1.errors], status=status.HTTP_400_BAD_REQUEST)



class NoteList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self,request, format=None):
        #notes = Note.objects.all()
        if request.user.is_anonymous():
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        elif request.user:
            notes=Note.objects.filter(user_id=request.user)
            serializer = NoteListSerializer(notes, many=True)
            return  Response(serializer.data)
        else:
          return Response({}, status=status.HTTP_400_BAD_REQUEST)


    def post(self,request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetail(APIView):

    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        print((request.user.id))
        if request.user.id == note.user_id:
            serializer = NoteSerializer(note)
            return Response(serializer.data)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        if request.user.id == note.user_id:
            serializer = NoteSerializer(note, data=request.data, partial=True)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, fromat=None):
        note = self.get_object(pk)
        if request.user.id == note.user_id:
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

#{"first_name":"aloha", "last_name": "aloha", "username":"aloha", "email":"aloha@alo.ha", "password": "12345678"}

