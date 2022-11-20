from django.db import models


class TaskStatus(models.Model):
    status           = models.CharField(max_length=50 , null = True , blank = True)

    def __str__(self):
        return self.status
    

class Task(models.Model):
    task_name       = models.CharField(max_length = 1000 , null = True , blank = True)
    task_status     = models.ForeignKey(TaskStatus, name="task_status", on_delete=models.CASCADE)
    created_at      = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task_name
    