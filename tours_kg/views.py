from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from tours_kg.models import *
from tours_kg.forms import BookNowForm


class MyQ(Q):
    default = 'OR'


class BaseView(View):
    def get(self, request, *args, **kwargs):
        regions = Region.objects.all()
        sights = Sight.objects.all()
        review = Review.objects.all()
        context = {
            'regions': regions,
            'sights': sights,
            # 'books': self.books,
            'review': review
        }
        return render(request, 'index.html', context)


class ReviewView(View):
    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all()
        context = {
            'review': reviews
        }
        return render(request, 'index.html', context)


def BookRightNow(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']
        sightseeing = request.POST['sightseeing']
        date = request.POST['date']
        quantity = request.POST['quantity']
        print(name, email, phone, date)
        ins = BookNow(name=name, surname=surname, email=email, phone=phone, date=date, sightseeing=sightseeing, quantity=quantity)
        ins.save()
        # messages.add_message(request, messages.INFO, 'Спасибо за бронь! Менеджер с Вами свяжется')
        return render(request, 'book.html')
    else:
        return render(request, 'book.html')
