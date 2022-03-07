from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELD = ['title']
