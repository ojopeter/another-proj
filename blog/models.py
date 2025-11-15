from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

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
    slug = models.SlugField(max_length=250,unique=True)
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
    
    #this is a code to automatically slugify a stuff
    
    # This is a way to slug
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{num}'
                num+=1
            self.slug = slug
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse("blog:blog_detail",args=[self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    