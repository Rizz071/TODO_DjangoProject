from django.contrib import admin

# Register your models here.
from .models import TodoList, TodoTitle

admin.site.register(TodoList)
admin.site.register(TodoTitle)