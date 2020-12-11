from __future__ import unicode_literals
from django import forms
from .models import Genre, Book

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['title','artist','description','thumbnail','order']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['genre','title','thumbnail','description','order']