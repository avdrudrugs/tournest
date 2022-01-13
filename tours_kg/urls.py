from django.urls import path
from tours_kg.views import index

urlpatterns = [
    path('', index, name='base_view'),
]