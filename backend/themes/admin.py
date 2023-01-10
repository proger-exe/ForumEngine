from django.contrib import admin
from .models import Topic, Like, Category, SubCategory, Comment

admin.site.register(Topic)
admin.site.register(Like)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Comment)
