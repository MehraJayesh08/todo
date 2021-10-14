from django.db import models

class todoList(models.Model):
    todo_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 500)
    date = models.DateField()

    def __str__(self):
        return self.title
