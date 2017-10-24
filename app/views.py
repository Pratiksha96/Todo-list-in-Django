"""from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
from app.models import app


def add_task(request):
    if request.method=='POST':
        task_obj=app(task_job=request.POST.get('job'),user_id=request.session['user_id'])
        task_obj.save()
        return HttpResponseRedirect('/')
    else:
        data=RequestContext(request,{'fname':request.session['fname']})
        return render_to_response('add_task.html',data)

def edit_task(request,task_id):
    if request.method=='POST':
        task_obj=app.objects.filter(id=request.POST.get('id')).update(task_job=request.POST.get('job'))
        return HttpResponseRedirect('/')
    else:
        task_obj=app.objects.filter(id=task_id)
        data=RequestContext(request,{'fname':request.session['fname'],'task':task_obj[0]})
        return render_to_response('edit_task.html',data)

def delete_task(request,task_id):
    app.objects.get(id=task_id).delete()
    return HttpResponseRedirect('/')
"""

from django.shortcuts import render
from django.utils import timezone
from .models import Todo


def todo_list(request):
    tasks = Todo.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request , 'app/todo_list.html' , {'tasks': tasks})