from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<school_id>[0-9]+)/classes/$', views.classes, name='classes'),
    url(r'(?P<school_id>[0-9]+)/class/(?P<class_id>[0-9]+)/$', views.schoolclass, name='schoolclass'),
    url(r'(?P<school_id>[0-9]+)/class/(?P<class_id>[0-9]+)/add_hw$', views.add_hw, name='add_hw'),
    url(r'(?P<school_id>[0-9]+)/$', views.school, name='school'),
]
