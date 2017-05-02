from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^linhas/$', views.Linhas.as_view()),
    url(r'^linha/(?P<id>\d+)/$', views.Linha.as_view()),
    url(r'^criar/linha/$', views.CreateLinha.as_view()),
    url(r'^carros/$', views.Carros.as_view()),
    url(r'^carro/(?P<id>\d+)/$', views.Carro.as_view()),
    url(r'^criar/carro/$', views.CreateCarro.as_view()),
    url(r'^periodo/', include("periodo.api.urls")),
]