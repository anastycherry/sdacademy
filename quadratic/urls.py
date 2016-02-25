from django.conf.urls import include, patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.quadratic_results, name='quadratic_results'),
)
