from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    upvotes = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=500)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
