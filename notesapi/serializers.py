__author__ = 'oleksandr'

from django.contrib.auth.models import User
from notesapp.models import Note, UserProfile
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','password', 'email')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields=('birthday','phone_number')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
            model = Note
            fields = ('note_name', 'note_body','user','category', 'labels', 'color','text','permit')