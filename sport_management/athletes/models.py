from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Competition(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    participants = models.ManyToManyField(Athlete, related_name='competitions')

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.title} ({self.date})"

