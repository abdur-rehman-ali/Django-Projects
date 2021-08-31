from django.db import models

# Create your models here.
class ToDoListData(models.Model):
    task=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} : {self.task}"