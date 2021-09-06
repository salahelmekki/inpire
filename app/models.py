from django.db import models
# from django.db.models.base import Model

# Create your models here.
class Etudiant(models.Model):
    prenom = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    age = models.IntegerField(default=0)
    moyenne = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    # class Meta:
    #     ordering = ["moyenne"]