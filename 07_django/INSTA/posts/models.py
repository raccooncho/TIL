from django.db import models
from django_extensions.db.models import TimeStampedModel
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
from faker import Faker
from django.conf import settings
# from django.contrib.auth.models import User
# import os
# ENV = os.environ.get('ENVIRONMENT', 'development')
# if ENV == 'development':
#     from IPython import embed
#     from faker import Faker

faker = Faker()


# Create your models here.
class Post(TimeStampedModel):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            Post.objects.create(content=faker.text(120))


class Image(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
        blank=True,
        upload_to='posts/images',
        processors=[ResizeToFill(600, 600)],
        format='JPEG',
        options={ 'quality': 90, }
         )  # pip install pillow


class Comment(TimeStampedModel):
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
