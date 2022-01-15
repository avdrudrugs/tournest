from django.urls import path
from tours_kg.views import BookRightNow, Success, JoinUsNow

urlpatterns = [
    path('book-now/', BookRightNow, name='book_now'),
    path('book-now/success/', Success, name='book-now-success'),
    path('', JoinUsNow, name='join-us')
    ]
