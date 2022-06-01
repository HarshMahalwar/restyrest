from django.db import models

# Create your models here.


class student(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    name = models.CharField(max_length=200)
    objects = None

    def __str__(self):
        return self.name
