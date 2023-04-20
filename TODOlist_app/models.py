from django.db import models


# Create your models here.
class TodoTitle(models.Model):
    """Class of TODO_lists titles"""
    title = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)


class TodoList(models.Model):
    """Class of individual TODOs list"""
    todo_text = models.TextField()
    order_num = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.ForeignKey(TodoTitle, on_delete=models.CASCADE)

    class Meta:
        ordering = ('order_num',)



