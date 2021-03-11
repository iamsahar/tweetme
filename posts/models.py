from django.db import models
from django.utils import timezone

from django.urls import reverse
from django import template

from accounts.models import MyUser


AUTH_USER_MODEL = 'accounts.MyUser'


class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    favourite = models.ManyToManyField(AUTH_USER_MODEL, related_name='favourite', blank=True)
    bookmark = models.ManyToManyField(AUTH_USER_MODEL, related_name='bookmark', blank=True)
    upload_file = models.FileField(
        upload_to='upload_files/', blank=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('home')

    def total_favourites(self):
        return self.favourite.count()

    register = template.Library()
    @register.filter
    def name(self, splitter=" "):
        return self.content.split(splitter)

    @property
    def sorted_content_set(self):
        return self.content.order_by('total_favourites')


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=250)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('home')
