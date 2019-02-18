from django.forms import ModelForm, TextInput
from .models import Filme
from .models import Serie


class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control',
            'placeholder': 'informe o Nome'}),

            'dt_lancamento': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: 1998-12-28'}),

            'genero': TextInput(attrs={'class':'form-control',
            'placeholder': 'Gênero'}),

            'sinopse': TextInput(attrs={'class':'form-control',
            'placeholder': 'Sobre o Filme'}),
            
             'foto': TextInput(attrs={'class':'form-control'})
        }

class SerieForm(ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control',
             'placeholder': 'informe o Nome'}),

            'dt_lancamento': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: 1998-12-28'}),

            'genero': TextInput(attrs={'class':'form-control',
            'placeholder': 'Gênero'}),

            'quant_temporadas': TextInput(attrs={'class':'form-control',
            'placeholder': 'Temporadas'}),

            'sinopse': TextInput(attrs={'class':'form-control',
            'placeholder': 'Sobre a Série'})
        }