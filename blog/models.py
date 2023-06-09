from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import math


STATUS = ((0, "Draft"), (1, "Published"))

class Tag(models.Model):
    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    image = models.ImageField(null=True, blank=True)
    reading_time = models.PositiveIntegerField(default=0, editable=False)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        # Calculate reading time based on an average reading speed of 200 words per minute
        word_count = len(self.content.split())
        self.reading_time = math.ceil(word_count / 200)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"