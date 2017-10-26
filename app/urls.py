from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^task/(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
]