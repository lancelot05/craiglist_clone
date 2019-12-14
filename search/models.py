from django.db import models

# Create your models here.

class Find(models.Model):
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{}'.format(self.text)



