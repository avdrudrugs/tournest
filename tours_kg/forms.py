from django import forms
from django.contrib.auth import get_user_model
from tours_kg.models import BookNow, Review

User = get_user_model()


class BookNowForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = BookNow
        fields = (
            'name', 'surname', 'phone', 'quantity', 'email', 'sightseeing', 'date', 'quantity'
        )


class JoinUs(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        class Meta:
            model = JoinUs
            fields = 'email'


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = (
            'name', 'reviews'
        )
