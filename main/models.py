from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class About(models.Model):
    image = models.ImageField(upload_to='about')
    description = models.TextField()
    video = models.FileField(upload_to='about')
    social_media = models.FileField(upload_to='about')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.CharField(max_length=100)
    image = models.ImageField(upload_to='comments')
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Userr(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile')
    brith = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name


class Team(models.Model):
    image = models.ImageField(upload_to='team')
    full_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    portfolio_link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class ScoialMedia(models.Model):
    telegram_link = models.CharField(max_length=100)
    instagram_link = models.CharField(max_length=100)
    youtube_link = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=100)
    twitter_url = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=100)
    tik_tok_link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.telegram_link


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    mini_description = models.CharField(max_length=100)
    book_link = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
