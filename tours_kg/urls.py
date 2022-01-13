from django.urls import path
from tours_kg.views import *

urlpatterns = [
    path('', BaseView, name='base_view'),
    path('', BookNow, name='book_now')
]