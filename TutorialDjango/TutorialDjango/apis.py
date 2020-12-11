# -- coding: utf-8
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
from .serializers  import GenreSerializer, BookSerializer
from .models import Genre, Book
from rest_framework.renderers import JSONRenderer

class getCategories(APIView):
    def get(self, request):
        try:
            genres = Genre.objects.all()
            genreSerializies = GenreSerializer(genres, many=True)
            genreContent = JSONRenderer().render(genreSerializies.data)
            genreStream = BytesIO(genreContent)
            genresData = JSONParser().parse(genreStream)
            return Response({"code": "200",
                             "data": genresData,
                             "status": "success"
                             })

        except Genre.DoesNotExist:
            return Response({"code": "404",
                             "data": [],
                             "status": "Data not found"
                             })

    def pos(self, request):
        pass

class getBooks(APIView):
    def get(self, request):
        try:
            if 'cateId' in request.GET:
                genreid = request.GET["cateId"]
                genre = Genre.objects.get(pk=genreid)
                genre_books = genre.book_set.all()
                bookSerializies = BookSerializer(genre_books, many=True)
                bookContent = JSONRenderer().render(bookSerializies.data)
                bookStream = BytesIO(bookContent)
                booksData = JSONParser().parse(bookStream)
            return Response({"code": "200",
                             "data": booksData,
                             "status": "success"
                             })

        except Book.DoesNotExist:
            return Response({"code": "404",
                             "data": [],
                             "status": "Data not found"
                             })

    def pos(self, request):
        pass
