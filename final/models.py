from django.db import models

# Create your models here.
class Final(models.Model):
    body = models.TextField(max_length=1000)
    body1 = models.TextField(max_length=1000)
    body2 = models.TextField(max_length=1000)
    body3 = models.TextField(max_length=1000)
    body4 = models.TextField(max_length=1000)

    def __str__(self):
        return self.body
    def __str__(self):
        return self.body1
    def __str__(self):
        return self.body2
    def __str__(self):
        return self.body3
    def __str__(self):
        return self.body4

    