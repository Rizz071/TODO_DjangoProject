from django.db import models

# Create your models here.

# class TodoList(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     todo_item = db.Column(db.String)
#     order_num = db.Column(db.Integer)


class TodoList(models.Model):
    """Class of individual TODOs list"""
    todo_text = models.TextField()
    order_num = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

