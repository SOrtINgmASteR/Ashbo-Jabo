from django.forms import ModelForm
from .models import *


class PopularDestinationForm(ModelForm):
    class Meta:
        model = PopularDestination
        fields = '__all__'

