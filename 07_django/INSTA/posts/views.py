from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Post, HashTag
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .forms import PostModelForm, ImageModelForm, CommentModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseBadRequest


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
            # create HashTag
            content = post_form.cleaned_data.get('content')
            words = content.split()  # 띄어쓰기 기준으로 split
            for word in words:
                if word[0] == '#' and len(word) <= 21:
                    word = word[1:]
                    tag = HashTag.objects.get_or_create(content=word)  # (HashTag objects, True or False)
                    post.tags.add(tag[0])
                    if tag[1]:  # tag가 처음 만들어진 거라면
                        messages.add_message(request, messages.SUCCESS, f'"#{tag[0].content}"를 처음으로 추가하셨어요! XD')

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
    pages = ' '
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
        'pages': pages,
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
                # update HashTag
                post.tags.clear()  # 기존의 tag 다 날리기!
                content = post_form.cleaned_data.get('content')
                words = content.split()  # 띄어쓰기 기준으로 split
                for word in words:
                    if word[0] == '#' and len(word) <= 21:
                        word = word[1:]
                        tag = HashTag.objects.get_or_create(content=word)  # (HashTag objects, True or False)
                        post.tags.add(tag[0])
                        if tag[1]:  # tag가 처음 만들어진 거라면
                            messages.add_message(request, messages.SUCCESS, f'"#{tag[0].content}"를 처음으로 추가하셨어요! XD')
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
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
    # return render(request, 'posts/form.html', {

    #     'comment_form': comment_form,
    #
    # })


@login_required
@require_POST
def toggle_like(request, post_id):
    if request.is_ajax():
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        is_active = True
        if user in post.like_users.all():
            post.like_users.remove(user)
            is_active = False
        else:
            post.like_users.add(user)
        return JsonResponse({
            'likeCount': post.like_users.count(),
            'is_active': is_active,
        })
    else:
        return HttpResponseBadRequest()


# def delete_like(request, post_id):
#     post = get_object_or_404(Post, post_id)
#     user = request.user
#     if user in post.like_users.all():   #filter(id=user.id):
#         post.like_users.remove(user)
#
#     pass

@require_GET
def tag_posts_list(request, tag_name):
    tag = get_object_or_404(HashTag, content=tag_name)
    posts = tag.posts.all()
    comment_form = CommentModelForm()
    pages = '#' + tag.content
    context = {'posts': posts, 'comment_form': comment_form, 'pages': pages}
    return render(request, 'posts/list.html', context)