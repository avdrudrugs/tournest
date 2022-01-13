from django.urls import path
from tours_kg.views import BaseView

urlpatterns = [
    path('', BaseView.as_view(), name='base_view'),
]