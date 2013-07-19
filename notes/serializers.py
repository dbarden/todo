# Django imports

# Contrib imports
from rest_framework import serializers
# Python imports

# Local imports
from notes.models import (Note, List)


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'name', 'notes')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
