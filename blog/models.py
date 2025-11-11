from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Published(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class David(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author__username='davido')
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF','Draft'
        PUBLISHED = 'PB','Published'
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    body = models.TextField(default='Enter Post')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    published =Published()
    david = David()
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
        
    def __str__(self):
        return self.title
    