from django.shortcuts import render
from . models import Filme
from . models import Serie

def home(request):
    return render(request, 'home.html',{})

def filme_list(request):
    filmes = Filme.objects.all()
    return render(request,'filme/list.html',{'filmes':filmes})

def filme_show(request, filme_id):
    filme = Filme.objects.get(pk=filme_id)
    return render(request,'filme/show.html',{'filme':filme})

def serie_list(request):
    series = Serie.objects.all()
    return render(request, 'serie/list.html',{'series':series}) 

def serie_show(request, serie_id):
    serie = Serie.objects.get(pk=serie_id)
    return render(request,'serie/show.html',{'serie':serie})