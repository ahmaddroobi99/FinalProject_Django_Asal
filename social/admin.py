from django.contrib import admin
from .models import Post, UserProfile,Comment

admin.site.register(Post)
admin.site.register(Comment)

admin.site.register(UserProfile)


# Register your models here.
