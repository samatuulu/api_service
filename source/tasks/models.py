from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Name')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Description')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    tag = models.ManyToManyField(Tag, related_name="tag_task", verbose_name="Tag for task")

    def __str__(self):
        return self.name