from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .forms import PostModelForm


# Create your views here.
@require_http_methods(['POST', 'GET'])
def post_create(request):
    # get 방식으로 data를 입력할 form 요청.
    if request.method == 'GET':
        form = PostModelForm()
    # post 방식으로 입력받은 data를 저장
    else:
        # POST 방식으로 넘어온 Data 를 ModelForm 에 넣는다.
        form = PostModelForm(request.POST, request.FILES)
        # Data 검증을 한다.
        if form.is_valid():
            # 통과하면 저장한다.
            form.save()
            return redirect('posts:post_list')
    # 실패하면, 다시 data 입력 form 을 준다.
    return render(request, 'posts/form.html', {
        'form': form,
    })


@require_GET
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {
        'posts': posts,
    })


@require_http_methods(['GET', 'POST'])
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
    else: form = PostModelForm(instance=post)
    return render(request, 'posts/form.html', {
        'form': form,
    })

