from django.urls import path
from .views import BookList


urlpatterns = [
    # path('books',books,name='books'),
    path('books',BookList.as_view(),name = 'books')
]
