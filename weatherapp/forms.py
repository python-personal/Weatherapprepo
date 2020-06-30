from django.forms import ModelForm,TextInput
from . models import Data

class CityForm(ModelForm):
    class Meta:
        model=Data
        fields=['name']
        # widgets={'name':TextInput(attrs={'class':input,'placeholder':'City Name'})}
