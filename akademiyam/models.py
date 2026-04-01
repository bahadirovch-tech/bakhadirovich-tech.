from django.db import models

class Kurs(models.Model):
    nomi = models.CharField(max_length=200)
    tavsifi = models.TextField()
    narxi = models.CharField(max_length=50, default="Bepul")
    
    def __str__(self):
        return self.nomi