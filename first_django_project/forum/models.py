import datetime
from django.db import models
from django.utils import timezone
import uuid

class User(models.Model):
    user_nickname = models.CharField(max_length=20)
    user_creation_date = models.DateTimeField()
    user_rating = models.PositiveSmallIntegerField(null=True, blank=True)
    user_articles_number = models.IntegerField(null=True,blank=True)
    user_comments_number = models.IntegerField(null=True, blank=True)
    user_avatar = models.ImageField(null=True, blank=True)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user_nickname

    

class Article(models.Model):
    article_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=50)
    article_text = models.TextField()
    article_creation_date = models.DateTimeField()
    article_rating = models.BooleanField(null=True)
    article_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f'{self.article_title} from {self.article_creator}'

    def article_was_published_recently(self):
        return self.article_creation_date >= (timezone.now() - datetime.timedelta(days=7))

class Comment(models.Model):
    comment_autohor = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_creation_date = models.DateTimeField()
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.comment_autohor

    def comment_was_published_recently(self):
        return self.comment_creation_date >= (timezone.now() - datetime.timedelta(days=7))
