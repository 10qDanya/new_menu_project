from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('self', null=True, blank=True, related_name='child', on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    named_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name