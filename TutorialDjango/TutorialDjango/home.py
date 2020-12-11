from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Book
from .forms import BookForm, GenreForm
from django.urls import reverse

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        categories = Genre.objects.all()
        books = Book.objects.all()
        return render(request, 'HomePage/index.html', {'categories': categories, 'books': books})

def addbook(request):
        form = BookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect(reverse('index'))
        context = {
            "form": form,
        }
        return render(request, 'HomePage/add_book.html', context)

def addGenre(request):
    form = GenreForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.save()
        return redirect(reverse('index'))
    context = {
        "form": form,
    }
    return render(request, 'HomePage/add_genre.html', context)

def updateBook(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid():
        book = form.save(commit=False)
        book.save()
        return redirect(reverse('index'))
    context = {
        "form": form,
    }
    return render(request, 'HomePage/add_book.html', context)

def deleteBook(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()

    categories = Genre.objects.all()
    books = Book.objects.all()
    return render(request, 'HomePage/index.html', {'categories': categories, 'books': books})