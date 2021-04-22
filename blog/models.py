from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE) # if user is deleted , their posts also get deleted

    def __str__(self):  # to change how we want to display object on shell (opt)
        return self.title

    # for returning url of newly created post as a string so that view can use it
    def get_absolute_url(self):
        return reverse('post-detail' , kwargs = {'pk':self.pk})