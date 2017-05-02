from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<mes>\d{2})/(?P<ano>\d{4})/$', views.Dias.as_view()),
    url(r'^folga/(?P<mes>\d{2})/(?P<ano>\d{4})/$', views.DiasFolga.as_view()),
    url(r'^dia/(?P<id>\d+)/$', views.Dia.as_view()),
    url(r'^criar/dia/$', views.CreateDia.as_view()),
]