from django.contrib import admin
from .models import Post, Categories, Profile, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Profile)
admin.site.register(Comment)