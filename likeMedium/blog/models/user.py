from django.db import models
import uuid


class User(models.Model):
    nickname = models.CharField(max_length=20)
    creation_date = models.DateTimeField()
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    articles_number = models.IntegerField(null=True,blank=True)
    comments_number = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.nickname