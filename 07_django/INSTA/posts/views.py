from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .forms import PostModelForm, ImageModelForm, CommentModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
@require_http_methods(['POST', 'GET'])
def post_create(request):
    # get 방식으로 data를 입력할 form 요청.
    if request.method == 'GET':
        post_form = PostModelForm()
        # image_form = ImageModelForm()
    # post 방식으로 입력받은 data를 저장
    else:
        # POST 방식으로 넘어온 Data 를 ModelForm 에 넣는다. image file 을 받으려면 request.FILES 를 해야한다.
        # form = PostModelForm(request.POST, request.FILES)
        post_form = PostModelForm(request.POST)

        # image_form = ImageModelForm(request.FILES)

        # post = Post()
        # post.content = request.POST.get('content')
        # post.title = request.POST.get('title')
        # post.score = request.POST.get('score')
        #
        # post.image = request.FILES.get('image')

        # Data 검증을 한다.
        if post_form.is_valid():
            # 통과하면 저장한다.
            post = post_form.save(commit=False)
            post.writer = request.user
            post.save()
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('posts:post_list')
    # 실패하면, 다시 data 입력 form 을 준다.
    image_form = ImageModelForm()
    return render(request, 'posts/form.html', {
        'post_form': post_form,
        'image_form': image_form,
    })


@require_GET
def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
    })


@login_required 
@require_http_methods(['GET', 'POST'])
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.writer == request.user:  # 지금 수정하려는 post 작성자가 요청보낸 사람이 맞는지?
        if request.method == 'POST':
            post_form = PostModelForm(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                return redirect('posts:post_list')
        else:
            post_form = PostModelForm(instance=post)
    # 작성자와 요청보낸 user가 다르다면,
    else:
        # 403 : Forbidden 금지됨!
        return redirect('posts:post_list')
    return render(request, 'posts/form.html', {
        'post_form': post_form,
    })


@login_required
@require_POST
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentModelForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.writer = request.user
        comment.post = post
        comment.save()
        return redirect('posts:post_list')
    # return render(request, 'posts/form.html', {
    #     'comment_form': comment_form,
    #
    # })