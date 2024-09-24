from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Task list and form to add new tasks
def task_list(request):
    tasks = Task.objects.all()  # Ensure you're querying the correct model
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
 
    return render(
        request,
        'tasks/task_list.html',
        {'tasks': tasks, 'form': form}  # Ensure 'tasks' is passed to the template
    )


# Editing an existing task
def tasks_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    
    return render(
        request,
        'tasks/task_edit.html',  # Use a separate template for editing
        {'form': form, 'task': task}
    )

# Deleting a task
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
