from django.db import models
from common.models.BaseModel import BaseModel
from django.contrib.auth.models import PermissionMixin, AbstractBaseUser


class User(AbstractUser, BaseModel):
    nickname = models.CharField(max_length=20)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    articles_number = models.IntegerField(null=True,blank=True)
    comments_number = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nickname
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'
