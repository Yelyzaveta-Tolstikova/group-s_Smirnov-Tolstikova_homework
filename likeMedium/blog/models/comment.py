import datetime
from django.db import models
from django.utils import timezone
from djangoProject.likeMedium.blog.models.user import User


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.author
