"""TutorialDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from . import home
from . import apis

app_name = 'TutorialDjango'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home.index, name='index'),
    path('addbook', home.addbook, name='addbook'),
    path('updatebook/(?P<book_id>\w+)', home.updateBook, name="updatebook"),
    path('deletebook/(?P<book_id>\w+)', home.deleteBook, name="deletebook"),
    path('addgenre', home.addGenre, name='addgenre'),
    path('api/category', apis.getCategories.as_view()),
    path('api/books', apis.getBooks.as_view()),
    path('login', views.login_user, name='login'),
]
