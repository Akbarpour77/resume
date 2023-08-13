from django.shortcuts import render, redirect
from Todo_app.forms import Todo_form
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime
from Todo_app.models import Todo


# Create your views here.

@login_required
def add(request):
    if request.method == 'POST':
        todo = Todo_form(request.POST)
        if todo.is_valid():
            todo_data = todo.save(commit=False)
            todo_data.created_at = datetime.today().strftime('%Y-%m-%d')
            todo_data.updated_at = datetime.today().strftime('%Y-%m-%d')
            todo_data.user_id = request.user.id
            todo_data.save()
            return redirect(reverse('base'))
    else:

        form_todo = Todo_form()

    return render(request, 'Todo.html', {'forms': form_todo})


@login_required
def show(request):
    user = request.user
    context = Todo.objects.get()

    return render(request, 'show.html', {'context': context, 'user': request.user.id})
