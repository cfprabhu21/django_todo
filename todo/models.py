from django.db import models


# Create your models here.
class TodoList(models.Model):
    """This is a todolist model class here we store all todolist data"""
    todo_title = models.CharField('Todo Title', max_length=250, blank=False, null=False)
    is_done = models.BooleanField('Done', default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add will set time when an instance is created
    updated_at = models.DateTimeField(auto_now=True)  # whereas auto_now will set time when someone modified

    class Meta:
        db_table = 'todo_list'
        verbose_name = 'todo_list'
        verbose_name_plural = 'todo_list'

    def __str__(self):
        return f"{self.todo_title}"
