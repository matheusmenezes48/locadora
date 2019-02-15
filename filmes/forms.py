from django.forms import ModelForm, TextInput
from .models import Filme
from .models import Serie


class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'dt_lancamento': TextInput(attrs={'class':'form-control'}),
            'genero': TextInput(attrs={'class':'form-control'}),
            'sinopse': TextInput(attrs={'class':'form-control'})
        }

class SerieForm(ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'dt_lancamento': TextInput(attrs={'class':'form-control'}),
            'genero': TextInput(attrs={'class':'form-control'}),
            'quant_temporadas': TextInput(attrs={'class':'form-control'}),
            'sinopse': TextInput(attrs={'class':'form-control'})
        }