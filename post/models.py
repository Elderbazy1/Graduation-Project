from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post (models.Model):
    titel = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)
    Description = RichTextField()
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    Category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now)
    vie_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    dislikes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titel

    class Meta:
        ordering = ['-publish_date']


class comment(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_at']


class Replay(models.Model):
    comment = models.ForeignKey(comment,on_delete=models.CASCADE)
    text = models.TextField()
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Like_dislike (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    likt = models.BooleanField()

