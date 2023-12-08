from django.shortcuts import render, redirect

from .models import Task




# Create your views here.
def home(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority')
        task = Task(task_name=name, priority=priority)
        task.save()
        return redirect('/')
    return render(request, 'home.html', {'task': task1})


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')
