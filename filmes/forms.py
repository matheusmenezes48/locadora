from django.forms import ModelForm, TextInput
from .models import Filme
from .models import Serie


class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: Homem Aranha'}),

            'dt_lancamento': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: 2005-04-25'}),

            'genero': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: Ação'}),

            'sinopse': TextInput(attrs={'class':'form-control',
            'placeholder': 'Sobre o Filme'}),
            

        }

class SerieForm(ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control',
             'placeholder': 'Exemplo: Shadowhantles'}),

            'dt_lancamento': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: 1998-12-28'}),

            'genero': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: Terror'}),

            'quant_temporadas': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: 4'}),

            'sinopse': TextInput(attrs={'class':'form-control',
            'placeholder': 'Sobre a Série'})
        }