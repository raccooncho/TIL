from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import CustomUserAuthenticationForm, CustomUserCreateForm
from posts.forms import CommentModelForm


# from django.contrib.auth import get_user_model

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'posts:post_list')
    else:
        form = CustomUserCreateForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    # 우선, 사용자가 로그인 되어 있는지?
    if request.user.is_authenticated:
        return redirect('posts:post_list')
    # 만약 로그인 되어있지 않다면,
    if request.method == 'POST':  # 사용자가 로그인 데이터를 넘겼을 때
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Do Log in
            user = form.get_user()
            auth_login(request, form.get_user())
            messages.add_message(request, messages.SUCCESS, f'Wecome {user.username}')
            messages.add_message(request, messages.INFO, f'Last login : {user.last_login}')
            return redirect('posts:post_list')
    # 사용자가 로그인 화면을 요청할 때
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })


@login_required
def logout(request):
    auth_logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout Successfully')
    return redirect('posts:post_list')


def user_detail(request, username):
    user_info = User.objects.get(username=username)
    comment_form = CommentModelForm()
    return render(request, 'accounts/user_detail.html', {'user_info': user_info, 'comment_form': comment_form})


@login_required
@require_POST
def toggle_follow(request, username):
    sender = request.user
    receiver = get_object_or_404(User, username=username)
    if sender != receiver:
        if receiver in sender.followings.all():
            sender.followings.remove(receiver)
        else:
            sender.followings.add(receiver)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))

