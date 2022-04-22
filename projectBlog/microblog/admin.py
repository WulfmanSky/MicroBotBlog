from django.contrib import admin
from .models import BlogProject, BlogPost, BlogImage, BlogVideo

admin.site.register(BlogProject)
admin.site.register(BlogPost)
admin.site.register(BlogImage)
admin.site.register(BlogVideo)
