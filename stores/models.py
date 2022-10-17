from django.db import models


class StoreItem(models.Model):
    class ItemKind(models.TextChoices):
        breakfast = "BR"
        lunch = "LU"
        dinner = "DI"

    name = models.CharField(max_length=35)
    description = models.TextField()
    kind = models.CharField(max_length=2, choices=ItemKind.choices)
    price = models.FloatField()
    image = models.TextField(default="")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
   
    