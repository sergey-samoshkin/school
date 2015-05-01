from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<school_id>[0-9]+)/', views.school, name='school'),
    url(r'(?P<school_id>[0-9]+)/classes/', views.classes, name='classes'),
]

