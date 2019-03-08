from django.shortcuts import render, get_object_or_404, redirect
from .models import Model

def list(request):
    my_models = Model.objects.all()
    context = {'my_models': my_models}
    return render(request, my_model/list.html, context)

def detail(request, id):
    my_model = get_object_or_404(Model, id=id)
    return render(request, my_model/detail.html, {'my_model': my_model})

def delete(request, id):
    if request.method == "POST":
        my_model = Model.objects.get(id=id)
        my_model.delete()
    return redirect('my_model:list')


-------------------------------------------------------------------
from django.urls import path
from . import views

app_name = 'my_model'

urlpatterns=[
    path('', views.list, name='list'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/delete/', views.delete, name='delete'),
]

-------------------------------------------------------------------

from djange.db import models

class my_model(models.Model):
    ...and

-------------------------------------------------------------------