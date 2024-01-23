from django.db.models import Avg, Count, Func, IntegerField
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View
from tours_kg.models import *
from tours_kg.forms import BookNowForm, JoinUsForm, ReviewForm


class BaseView(View):

    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all()
        tours = Sight.objects.annotate(avg_rating=Func(Avg('review__rating'), function="ROUND",
                                                       output_field=IntegerField()),
                                       total_reviews=Count('review__rating'))
        images = Image.objects.all()
        context = {
            'reviews': reviews,
            "tours": tours,
            "images": images,
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        join = JoinUsForm
        email = request.POST['email']
        all_email = JoinUs(email=email)
        all_email.save()
        return render(request, 'index.html', {'join': join})


def BookRightNow(request, *args, **kwargs):
    form = BookNowForm

    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']
        sightseeing = request.POST['sightseeing']
        date = request.POST['date']
        quantity = request.POST['quantity']
        ins = BookNow(name=name, surname=surname, email=email, phone=phone, date=date, sightseeing_id=sightseeing,
                      quantity=quantity)
        ins.save()
        if ins.save() == ins.save():
            return HttpResponseRedirect('success/')
        return render(request, 'book.html', {'form': form})
    else:

        return render(request, 'book.html', {'form': form})


def Success(request):
    return render(request, 'success.html')


def save_comment(request, *args, **kwargs):
    form = ReviewForm

    if request.method == 'POST':
        name = request.POST['name']
        review = request.POST['reviews']
        rating = request.POST['rating']
        sight = request.POST['sight']
        coms = Review(name=name, reviews=review, rating=rating, sight_id=sight)

        coms.save()
        if coms.save() == coms.save():
            return HttpResponseRedirect('/')
        return render(request, 'index.html', {'form': form})
    else:
        return render(request, 'index.html', {'form': form})


def sight_detail(request, slug):
    sight = get_object_or_404(Sight, slug=slug)
    return render(request, 'sight_detail.html', {'sight': sight})
