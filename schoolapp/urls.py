from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<pk>[0-9]+)/classes/$', views.ClassList.as_view(), name='classes'),
    url(r'(?P<school_id>[0-9]+)/class/(?P<pk>[0-9]+)/$', views.SchoolClassView.as_view(), name='schoolclass'),
    url(r'(?P<school_id>[0-9]+)/class/(?P<class_id>[0-9]+)/add_hw$', views.add_hw, name='add_hw'),
    url(r'(?P<school_id>[0-9]+)/class/(?P<class_id>[0-9]+)/download_hw/(?P<hw_id>[0-9]+)$', views.download_hw, name='download_hw'),
    url(r'(?P<pk>[0-9]+)/$', views.SchoolView.as_view(), name='school'),
]
