from django import forms
from django.contrib.auth import get_user_model
from tours_kg.models import BookNow, Sight

User = get_user_model()


class BookNowForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookNowForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    sightseeing = forms.Select(attrs={'class': 'form-control'},
                               choices=BookNow.TOURS)

    class Meta:
        model = BookNow
        fields = ('__all__')


class JoinUs(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        class Meta:
            model = JoinUs
            fields = 'email'
