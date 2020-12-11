from rest_framework import serializers
from .models import Genre, Book

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title', 'thumbnail', 'description', 'order', 'time_stamp')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title',  'thumbnail', 'description', 'order')