from django.views.generic import View
from tours_kg.models import BookNow

class BookMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer =  Users.objects.filter(user=request.user).first()
            if not customer:
                customer = customer.objects.create(
                    user=request.user
                )
                books = Books.objects.filter()


        else:
            books = Books.objects.filter(for_anonymous_user=True).first()
            if not books:
                books = Books.objects.create(for_anonymous_user=True)
        self.books = books
        return super().dispatch(request, *args, **kwargs)
