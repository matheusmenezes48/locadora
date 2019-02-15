from django.shortcuts import render, redirect
from . models import Filme
from . models import Serie
from .forms import FilmeForm
from .forms import SerieForm

def home(request):
    return render(request, 'home.html',{})

def filme_list(request):
    filmes = Filme.objects.all()
    return render(request,'filme/list.html',{'filmes':filmes})

def filme_show(request, filme_id):
    filme = Filme.objects.get(pk=filme_id)
    return render(request,'filme/show.html',{'filme':filme})

def form_filme(request):
    if (request.method == 'POST'):
        form = FilmeForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/filmes/filme')
        else:
            return render(request,'filme/form.html',{'form':form})
    else:
        form = FilmeForm()
        return render(request,'filme/form.html',{'form':form})

def serie_list(request):
    series = Serie.objects.all()
    return render(request, 'serie/list.html',{'series':series}) 

def serie_show(request, serie_id):
    serie = Serie.objects.get(pk=serie_id)
    return render(request,'serie/show.html',{'serie':serie})

def form_serie(request):
    if (request.method == 'POST'):
        form = SerieForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/filmes/serie')
        else:
            return render(request,'serie/form.html',{'form':form})
    else:
        form = SerieForm()
        return render(request,'serie/form.html',{'form':form})