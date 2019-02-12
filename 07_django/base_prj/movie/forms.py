from django import forms
from .models import Movie


class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    title_eng = forms.CharField(max_length=100)
    audience = forms.IntegerField()
    open_dt = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )
    genre = forms.CharField(max_length=100)
    watch_grade = forms.CharField(max_length=100)
    score = forms.FloatField()
    poster_url = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__' # ['title', 'genre']
        widgets = {
            'open_dt': forms.DateInput(attrs={'type': 'date'})
        }

