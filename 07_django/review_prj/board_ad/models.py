from django.db import models


# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length=200, default='No Title')

    def __str__(self):
        return f'{self.id}: {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=200, default='No Comment')

    def __str__(self):
        return f'{self.id} comment'