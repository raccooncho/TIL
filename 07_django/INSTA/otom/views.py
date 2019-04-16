from django.shortcuts import render, redirect
from .models import Writer, Book, Chapter
from .forms import *


def create(request):
    if request.method == 'POST':
        form = WriterModelForm(request.POST)
        if form.is_valid():  # data 가 저장 가능??
            form.save()

    elif request.method == 'GET':
        form = WriterModelForm()
    return render(request, 'new.html', {
        'form': form
    })


def update(request, id):
    writer = Writer.objects.get(id=id)
    if request.method == 'POST':
        form = WriterModelForm(request.POST, instance=writer)
        if form.is_valid():
            form.save()
            return redirect('')
    elif request.method == 'GET':
        form = WriterModelForm(instance=writer)
    return render(request, 'edit.html', {
        'form': form
    })

