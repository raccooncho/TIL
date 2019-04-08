from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# Create your views here.

# id 불필요
def article_new(request):

    pass

def article_create(request):
    pass

def article_list(request):
    pass

# id 필요
def article_detail(request):
    pass

def article_edit(request):
    pass

def article_update(request):
    pass

def article_delete(request):
    pass














def index(request):
    return render(request, 'board/index.html')

def greeting(request, name, role):
    if role == 'admin':
        return render(request, 'board/greeting.html', {
            'name': name,
            'role': 'MASTER USER',
        })
    else:
        return render(request, 'board/greeting.html', { 'name': name, 'role': role })


