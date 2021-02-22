from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    author=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    url=models.URLField()


    def __str__(self):
        return self.title