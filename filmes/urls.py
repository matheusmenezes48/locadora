from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('filme/',views.filme_list),
    path('filme/<int:filme_id>/',views.filme_show),
    path('serie/',views.serie_list),
    path('serie/<int:serie_id>/',views.serie_show)
]