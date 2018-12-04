from django.db import models

class Url(models.Model):

    url = models.CharField(max_length=255)
    shorturl = models.CharField(max_length=15,unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        super(Url,self).save(*args, **kwargs)

    def my_self(self):
        super(Url,self).save(*args,**kwargs)

    def __str__(self):
        return self.url
