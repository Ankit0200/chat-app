from django.db import models

class chat(models.Model):
    message = models.CharField(max_length=1000)
    timestamp= models.DateTimeField(auto_now_add=True)
    group=models.ForeignKey('Group', on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
