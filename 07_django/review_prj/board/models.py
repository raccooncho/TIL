from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='write contents')

    def __str__(self):
        return f'{self.id}: {self.title}'