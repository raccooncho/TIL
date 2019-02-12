from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100, default='')
    audience = models.IntegerField(default=0)
    open_dt = models.DateField()
    genre = models.CharField(max_length=100, default='')
    watch_grade = models.CharField(max_length=100, default='')
    score = models.FloatField(default=0.0)
    poster_url = models.TextField(default='')
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.title}'

