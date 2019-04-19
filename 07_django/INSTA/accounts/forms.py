from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
# 1 회원가입 / 2 회원 정보 수정 / 3 로그인
from .models import User


class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')  # ['username', 'email', ]


class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User
        fields = ('username', 'email')

