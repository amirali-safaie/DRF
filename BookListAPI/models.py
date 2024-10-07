from django.db import models

class Book(models.Model):
    title = models.CharField(
        max_length = 255,
    )

    author = models.CharField(
        max_length = 255,
    )

    price = models.DecimalField(
        max_digits = 5,
        decimal_places = 2
    )

    class Meta:
        managed = True
        indexes = [models.Index(fields=['price']),]
    
    def __str__(self) -> str:
        return self.title