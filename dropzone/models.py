from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Images"

    def __str__(self):
        return self.image
