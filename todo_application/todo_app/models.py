from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    """ Model for storing tasks in which """
    user = models.ForeignKey(User, null=True, related_name='parent_user', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
        indexes = [
            models.Index(fields=['title'])]
