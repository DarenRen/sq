from django.forms import ModelForm

from .models import Sq

class SqForm (ModelForm):
    class Meta:
        model = Sq
        fields = '__all__'
