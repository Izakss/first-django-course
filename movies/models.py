from django.db import models

class Movie(models.Model):
    title = models.CharField(verbose_name="title", max_length=200)
    year =models.IntegerField(verbose_name="year", default=0)


    def __str__(self):
        return f'{self.title} from {self.year}'