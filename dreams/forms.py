from django.forms import ModelForm
from .models import Dreams


class DreamsForm(ModelForm):
    class Meta:
        model = Dreams
        fields = ["counter"]
