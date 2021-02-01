from django.db import models
from django.utils import timezone


class Article(models.Model):
    choises = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    title = models.CharField(max_length=255)
    slog = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=choises)
    def __str__(self):
        return self.title
