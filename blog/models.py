from django.db import models

# Create your models here.


class Place(models.Model):
    id_place = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return self.id_place


class Simpson(models.Model):
    id_character = models.CharField(max_length=100, primary_key=True)
    surnom = models.CharField(max_length=20)
    etat = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_character
