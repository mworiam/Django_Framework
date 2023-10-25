from django.shortcuts import render, redirect
from .models import TodoItem
from django.views.decorators.http import require_POST

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

@require_POST
def add_todo(request):
    title = request.POST['title']
    todo = TodoItem(title=title)
    todo.save()
    return redirect('todo_list')

def complete_todo(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def delete_completed(request):
    TodoItem.objects.filter(completed=True).delete()
    return redirect('todo_list')

def delete_all(request):
    TodoItem.objects.all().delete()
    return redirect('todo_list')
