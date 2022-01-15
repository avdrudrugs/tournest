from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from tours_kg.models import *
from tours_kg.forms import BookNowForm, JoinUsForm
from django.contrib import messages


class MyQ(Q):
    default = 'OR'


class BaseView(View):
    def get(self, request, *args, **kwargs):
        regions = Region.objects.all()
        sights = Sight.objects.all()
        context = {
            'regions': regions,
            'sights': sights,
            # 'books': self.books,
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
        if ins.save() == ins.save():
            return HttpResponseRedirect('success/')
        return render(request, 'book.html', {'form': form})
    else:
        return render(request, 'book.html', {'form': form})


def Success(request):
    return render(request, 'success.html')


def JoinUsNow(request, *args, **kwargs):
    join = JoinUsForm
    if request.method == 'POST':
        email = request.POST['email']
        all_email = JoinUs(email=email)
        all_email.save()
        return render(request, 'index.html', {'join': join})
    else:
        return render(request, 'index.html', {'join': join})
# def JoinUsNow(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form_email = JoinUsForm(request.POST)
#         # check whether it's valid:
#         if form_email.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/')
#
#     # if a GET (or any other method) we'll create a blank form
#     return render(request, 'index.html', {'form_email': form_email})


# if 'service' in request.POST:
#     service = request.POST['service']
# else:
#     service = False
