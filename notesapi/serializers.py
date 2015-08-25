__author__ = 'oleksandr'

from django.contrib.auth.models import User
from notesapp.models import Note, UserProfile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(allow_blank=False)
    last_name = serializers.CharField(allow_blank=False)
    username = serializers.CharField(allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})
    email = serializers.EmailField(allow_blank=False)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','password', 'email')

class UserProfileSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    birthday = serializers.DateField()
    phone_number = serializers.CharField(max_length=11)
    class Meta:
        model = UserProfile
        fields=('birthday','phone_number')


class NoteListSerializer(serializers.ModelSerializer):
    class Meta:
            model = Note
            fields = ("id", "note_name")

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
            model = Note
            fields = ('id','note_name', 'note_body','user','category', 'labels', 'color','text','permit')