from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from tours_kg.models import *
from tours_kg.forms import RegistrationForm


class MyQ(Q):
    default = 'OR'


class BaseView(View):
    def get(self, request, *args, **kwargs):
        regions = Region.objects.all()
        sights = Sight.objects.all()
        context = {
            'regions': regions,
            'sights': sights,
            'books': self.books
        }
        return render(request, 'index.html', context)

class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        regions = Region.objects.all()
        context = {
            'form': form,
            'regions': regions,
            'books':self.books
        }
        return render(request, 'index.html', context)
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Users.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone']
            )
            user = authenticate(
                username=new_user.username, password=form.cleaned_data['password']
            )
            login(request, user)
            return HttpResponseRedirect('/')
        regions = Region.objects.all()
        context = {
            'form':form,
            'regions': regions,
            'books':self.books
        }
        return render(request, 'index.html', context)



def index(request):
    return render(request, 'index.html')




