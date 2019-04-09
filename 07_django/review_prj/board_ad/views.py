from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment

# Create your views here.
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'board_ad/list.html', {
        'postings': postings
    })

def posting_detail(request, id):
    posting = Posting.objects.get(id=id)
    return render(request, 'board_ad/detail.html', {
        'posting': posting
    })

def posting_create(request):
    pass

def posting_edit(request, id):
    pass

def posting_delete(request, id):
    pass