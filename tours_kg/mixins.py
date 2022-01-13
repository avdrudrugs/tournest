from django.views.generic import View
from tours_kg.models import BookNow, Users


class BookMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            users = Users.objects.filter(user=request.user).first()
            if not users:
                customer = users.objects.create(
                    user=request.user
                )
            books = BookNow.objects.filter(owner=users, in_order=False).first()
            if not books:
                books = BookNow.objects.create(owner=users)
        else:
            books = BookNow.objects.filter(for_anonymous_user=True).first()
            if not books:
                books = BookNow.objects.create(for_anonymous_user=True)
        self.books = books
        return super().dispatch(request, *args, **kwargs)
