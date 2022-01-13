from django.urls import path
from tours_kg.views import BaseView, BookView

urlpatterns = [
    path('', BaseView.as_view(), name='base_view'),
    path('booking/', BookView.as_view(), name='book_view'),
]