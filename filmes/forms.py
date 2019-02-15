from django.forms import ModelForm, TextInput
from .models import Filme


class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'dt_lancamento': TextInput(attrs={'class':'form-control'}),
            'nome': TextInput(attrs={'class':'form-control'}),
            'sinopse': TextInput(attrs={'class':'form-control'}),
            'genero': TextInput(attrs={'class':'form-control'})
        }