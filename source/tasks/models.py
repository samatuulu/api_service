from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Description')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Name')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    task = models.ManyToManyField(Task, related_name='task_tag')

    def __str__(self):
        return self.name