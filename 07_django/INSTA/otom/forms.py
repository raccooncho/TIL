from django import forms
from .models import *


# Writer, Book, Chapter

class WriterModelForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = '__all__'  # or ['name']


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class ChapterModelForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'








