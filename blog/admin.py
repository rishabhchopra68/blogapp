from django.contrib import admin

from .models import Post
# Register your models here.

admin.site.register(Post) # to make it visible on admin page too , this is required

