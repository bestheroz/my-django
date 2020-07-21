from django.db import models


class Todo(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    text = models.CharField(max_length=1000)
    checked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
