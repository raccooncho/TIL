from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment
from django.views.decorators.http import require_http_methods

# Create your views here.
# Read
@require_http_methods(['GET'])
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'board_ad/list.html', {
        'postings': postings
    })

@require_http_methods(['GET'])
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all()
    return render(request, 'board_ad/detail.html', {
        'posting': posting,
        'comments': comments
    })
# Create
@require_http_methods(['GET', 'POST'])
def posting_create(request):
    if request.method == 'POST':
        posting = Posting()
        posting.title = request.POST.get('posting_title')
        if posting.title:
            posting.content = request.POST.get('posting_content')
            posting.save()
            return redirect('board_ad:posting_detail', posting_id=posting.id)
        else:
            return render(request, 'board_ad/create.html')
    else:
        return render(request, 'board_ad/create.html')
# Update
@require_http_methods(['GET', 'POST'])
def posting_update(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    title = posting.title
    if request.method == 'POST':
        posting.title = request.POST.get('posting_title')
        if not posting.title: posting.title = title
        posting.content = request.POST.get('posting_content')
        posting.save()
        return redirect('board_ad:posting_detail', posting_id=posting.id)
    else:
        return render(request, 'board_ad/update.html', {
            'posting': posting
        })
# Delete
@require_http_methods(['POST'])
def posting_delete(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('board_ad:posting_list')


# Comment - Create
@require_http_methods(['POST'])
def comment_create(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = Comment()
    comment.content = request.POST.get('comment_content')
    comment.posting = posting
    comment.save()
    return redirect('board_ad:posting_detail', posting_id=posting.id)

@require_http_methods(['POST'])
def comment_delete(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('board_ad:posting_detail', posting_id=posting.id)

