from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from django.template.loader import render_to_string


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            tasks = Task.objects.all()
            data['task_list'] = render_to_string(
                'tasklist.html', {'tasks': tasks})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

    else:
        form = TaskForm()
    return save_all(request, form, 'create.html')


def detail_task(request, pk):
    data = dict()
    task = get_object_or_404(Task, id=pk)
    data['form_is_valid'] = True
    data['task_list'] = render_to_string('detail.html', {'task': task})
    context = {
        'task': task
    }
    data['html_form'] = render_to_string(
        'detail.html', context, request=request)
    return JsonResponse(data)


def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

    else:
        form = TaskForm(instance=task)
    return save_all(request, form, 'update.html')


def delete_task(request, pk):
    data = dict()
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        task.delete()

        data['form_is_valid'] = True
        tasks = Task.objects.all()
        data['task_list'] = render_to_string('tasklist.html', {'tasks': tasks})
    else:
        context = {'task': task}
        data['html_form'] = render_to_string(
            'delete.html', context, request=request)

    return JsonResponse(data)
