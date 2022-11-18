from django.db import models

# Create your models here.

class SignUp(models.Model):
    username = models.CharField(max_length=16)
    email = models.EmailField()
    password1 = models.CharField(max_length=16)
    password2 = models.CharField(max_length=16)
    class Meta:
        app_label = 'vliplistore'


class Notes(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'vliplistore'