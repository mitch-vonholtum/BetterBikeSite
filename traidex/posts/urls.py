from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<entry_id>\d+)/detail', views.detail, name = 'detail'),
	url(r'^create/', views.create, name = 'create'),
)