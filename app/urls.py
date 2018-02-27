from django.conf.urls import url, include 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^todo/(?P<pk>\d+)/$', views.todo_detail, name='todo_detail'),
    url(r'^todo/new/$', views.todo_new, name='todo_new'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.todo_edit, name='todo_edit'),
    url(r'^todo/(?P<pk>\d+)/remove/$', views.todo_remove, name='todo_remove'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}),
    url(r'^logout/$', auth_views.logout, {'template_name': 'app/logout.html'}),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

]