from django.contrib import admin
from myapp.models import Blog

# Register your models here.
class AdminBlog(admin.ModelAdmin):
  list_display = ['id', 'author', 'title', 'desc', 'date']
  
admin.site.register(Blog, AdminBlog)