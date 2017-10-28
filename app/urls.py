from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^task/(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    url(r'^todo/new/$', views.todo_new, name='todo_new'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.todo_edit, name='todo_edit'),
   
]