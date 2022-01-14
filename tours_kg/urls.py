from django.urls import path
from tours_kg.views import *

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('book-now/', BookRightNow, name='book_now')
    ]
