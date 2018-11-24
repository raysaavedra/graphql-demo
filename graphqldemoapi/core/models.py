from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname


class Comment(models.Model):
    comment = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Comic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(Genre, related_name='genre', on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title