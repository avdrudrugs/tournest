from django.urls import path
from tours_kg.views import BookRightNow, Success, BaseView, save_comment, sight_detail

urlpatterns = [
    path('book-now/', BookRightNow, name='book_now'),
    path('book-now/success/', Success, name='book-now-success'),
    path('', BaseView.as_view(), name='base'),
    path('comment/', save_comment, name='save'),
    path('sights/<slug:slug>/', sight_detail, name='sight_detail'),
    ]
