from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^login/do/$', views.do_login_view, name='do_login'),
    url(r'^logout/do/$', views.do_logout_view, name='do_logout'),
    url(r'(?P<pk>[0-9]+)/classes/$', views.ClassList.as_view(), name='classes'),
    url(
        r'(?P<school_id>[0-9]+)/class/(?P<pk>[0-9]+)/$',
        login_required(views.SchoolClassView.as_view()),
        name='schoolclass'
    ),
    url(
        r'(?P<school_id>[0-9]+)/class/(?P<class_id>[0-9]+)/add_hw$',
        login_required(views.add_hw),
        name='add_hw'
    ),
    url(
        r'(?P<school_id>[0-9]+)/class/(?P<class_id>[0-9]+)/download_hw/(?P<hw_id>[0-9]+)$',
        login_required(views.download_hw),
        name='download_hw'
    ),
    url(r'(?P<pk>[0-9]+)/$', views.SchoolView.as_view(), name='school'),
]
