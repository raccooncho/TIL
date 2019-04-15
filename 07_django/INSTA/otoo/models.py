from django.db import models


# Create your models here.

class User(models.Model):
    email_address = models.EmailField(default='abc@abcd.com', unique=True)
    password = models.CharField(max_length=20, default='12345678$$')

    def __str__(self):
        return f'{self.id}: {self.email_address}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    last_name = models.CharField(max_length=50, default='Name')
    first_name = models.CharField(max_length=50, default='No')

    def __str__(self):
        return f"{self.id} : {self.user.email_address}'s profile"



