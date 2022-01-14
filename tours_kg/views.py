from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from tours_kg.models import *
from tours_kg.forms import BookNowForm
from django.contrib import messages


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
    form = BookNowForm

    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']
        sightseeing = request.POST['sightseeing']
        date = request.POST['date']
        quantity = request.POST['quantity']
        print(name, email, phone, date)
        ins = BookNow(name=name, surname=surname, email=email, phone=phone, date=date, sightseeing=sightseeing,
                      quantity=quantity)
        ins.save()
        messages.add_message(request, messages.INFO, 'Спасибо за бронь! Менеджер с Вами свяжется')
        return render(request, 'book.html', {'form': form})
    else:
        return render(request, 'book.html', {'form': form})


class BookView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'book.html')

# class RegistrationView(View):
#     def get(self, request, *args, **kwargs):
#         form = RegistrationForm(request.POST or None)
#         regions = Region.objects.all()
#         context = {
#             'form': form,
#             'regions': regions,
#             'books': self.books
#         }
#         return render(request, 'registration.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = RegistrationForm(request.POST or None)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.username = form.cleaned_data['username']
#             new_user.email = form.cleaned_data['email']
#             new_user.first_name = form.cleaned_data['first_name']
#             new_user.last_name = form.cleaned_data['last_name']
#             new_user.set_password(form.cleaned_data['password'])
#             new_user.save()
#             Users.objects.create(
#                 user=new_user,
#                 phone=form.cleaned_data['phone']
#             )
#             user = authenticate(
#                 username=new_user.username, password=form.cleaned_data['password']
#             )
#             login(request, user)
#             return HttpResponseRedirect('/')
#         regions = Region.objects.all()
#         context = {
#             'form': form,
#             'regions': regions,
#             'books': self.books
#         }
#         return render(request, 'registration.html', context)
