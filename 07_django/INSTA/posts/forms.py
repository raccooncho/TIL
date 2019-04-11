from django import forms
from .models import Post


class PostModelForm(forms.ModelForm):
    # content = forms.EmailField(label='Your email')
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['content', ... ]
