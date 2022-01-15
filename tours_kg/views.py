from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, View
from tours_kg.models import *
from tours_kg.forms import BookNowForm, ReviewForm
from django.core.exceptions import ObjectDoesNotExist
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
            'reviews': review
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
        ins = BookNow(name=name, surname=surname, email=email, phone=phone, date=date, sightseeing=sightseeing,
                      quantity=quantity)
        ins.save()
        # messages.add_message(request, messages.INFO, 'Спасибо за бронь! Менеджер с Вами свяжется')
        return render(request, 'book.html')
    else:
        return render(request, 'book.html')


def savecomment(request, *args, **kwargs):
    form = ReviewForm

    if request.method == 'POST':
        name = request.POST['name']
        reviews = request.POST['reviews']
        coms = Review(name=name, reviews=reviews)
        coms.save()
        return render(request, 'index.html', {'form': form})
    else:
        return render(request, 'index.html', {'form': form})




    # def home(request):
    #     if request.method == 'POST':
    #         id = request.POST.get('id', None)
    #         if id:
    #             try:
    #                 post = Post.objects.get(pk=id)
    #             except ObjectDoesNotExist:
    #                 return ()  # обработка ошибки пост не найден
    #             if form.is_valid():
    #                 form = form.save(commit=False)
    #                 form.user = request.user
    #                 form.post = post
    #                 form.save()
    #                 return ()  # все хорошо, коммент сохранен
    #             return ()  # обработка ошибки форма не валидная
    #         return ()  # обработка ошибки id не передан
    #     # else здесь не обязательно писать код выполнится только если не ПОСТ
    #     context = {
    #         'form': CommentForm(),
    #         'comments': Comment.objects.filter(moderation=True)
    #     }
    #     return (request, 'blog/index.html', context)  # return метод GET
