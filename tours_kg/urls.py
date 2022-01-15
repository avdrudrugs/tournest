from django.urls import path
from tours_kg.views import BaseView, BookRightNow, savecomment


urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('book-now/', BookRightNow, name='book_now'),
    path('comment/', savecomment, name='save'),
]