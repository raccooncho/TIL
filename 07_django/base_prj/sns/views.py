from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment


def posting_list(request):
    postings = Posting.objects.all()
    context = {
        'postings': postings,
    }
    return render(request, 'sns/list.html', context)


def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all()
    context = {
        'posting': posting,
        'comments': comments,
    }
    return render(request, 'sns/detail.html', context)

def create_posting(request):
    if request.method == 'POST':
        posting = Posting()
        posting.content = request.POST.get('content')
        posting.icon = request.POST.get('icon')
        posting.image = request.FILES.get('image')
        posting.save()
        return redirect('sns:posting_detail', posting.id)
    else:
        return redirect('sns:posting_list')

def edit_posting(request, posting_id):
    pass

def delete_posting(request, posting_id):
    pass

def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST.get('comment')
        comment.posting = posting
        comment.save()
    return redirect('sns:posting_detail', posting.id)