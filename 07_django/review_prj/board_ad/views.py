from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment

# Create your views here.
# Read
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'board_ad/list.html', {
        'postings': postings
    })

def posting_detail(request, id):
    posting = get_object_or_404(Posting, id=id)
    return render(request, 'board_ad/detail.html', {
        'posting': posting
    })

# Create
def posting_create(request):
    if request.method == 'POST':
        posting = Posting()
        posting.title = request.POST.get('posting_title')
        posting.content = request.POST.get('posting_content')
        posting.save()
        return redirect('board_ad:posting_detail', posting.id)
    else:
        return render(request, 'board_ad/create.html')

# Update
def posting_update(request, id):
    posting = get_object_or_404(Posting, id=id)
    if request.method == 'POST':
        posting.title = request.POST.get('posting_title')
        posting.content = request.POST.get('posting_content')
        posting.save()
        return redirect('board_ad:posting_detail', posting.id)
    else:
        return render(request, 'board_ad/update.html', {
            'posting': posting
        })

# Delete
def posting_delete(request, id):
    posting = get_object_or_404(Posting, id=id)
    if request.method == 'POST':
        posting.delete()
        return redirect('board_ad:posting_list')