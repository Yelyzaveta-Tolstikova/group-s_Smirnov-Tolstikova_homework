import uuid

from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    amount_of_articles = models.IntegerField(null=True, blank=True)
    amount_of_comments = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.nickname
