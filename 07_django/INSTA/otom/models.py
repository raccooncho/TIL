from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class MagazineArticle(TimeStampedModel, TitleDescriptionModel):
    content = models.TextField(default='NoContent')


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # Table 이 migrate되지 않음.


class Writer(TimeStamp):
    name = models.CharField(max_length=50, default='UNKNOWN')

    def __str__(self):
        return f'{self.id}: {self.name}'


class Book(TimeStamp):
    author = models.ForeignKey(Writer, on_delete=models.PROTECT)
    title = models.CharField(max_length=200, default="No Title", unique=True)

    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id}: {self.title}'


class Chapter(TitleDescriptionModel, TimeStampedModel):
    # title, description, created, modified
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.book.title} - {self.title}'