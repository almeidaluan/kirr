from django.db import models
import string
import random
from .utils import code_generator,create_shortcode
from django.conf import settings
from django.urls import reverse

SHORT_CODE_MAX = getattr(settings,"SHORTCODE_MAX",15)

class UrlManager(models.Manager):


    #Sobrescrevendo o all para retornar todas as urls que sao ativas
    def all(self,*args,**kwargs):
        qs  = super(UrlManager, self).all(*args,**kwargs)
        qs = qs.filter(active=True)
        return qs

    #Criando metodo para pegar urls que contenham .br e que sao ativas
    def getBr(self,*args,**kwargs):
        qs = super(UrlManager,self).all(*args,**kwargs)
        for u in qs:
            u.url = Url.objects.filter(url__icontains='.br')

        return print(u.url)

class Url(models.Model):

    url = models.CharField(max_length=SHORT_CODE_MAX)
    shorturl = models.CharField(max_length=15,unique=True,blank=True) # Blank Usado para evitar o erro de campo em branco na hora que manda salvar no admin
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = UrlManager() # ou eu posso criar um objects_random e atribuir urlManager dps fazer a chamada Url.objects_random.meumetodo
    #objects_random = UrlManager()

    #Sobrescrevendo comportamento do save normal
    def save(self, *args, **kwargs):
        if self.shorturl is None or self.shorturl == "":
            self.shorturl = create_shortcode(self)
        super(Url,self).save(*args, **kwargs)

    # def my_self(self):
    #     if self.shorturl is None or self.shorturl == "":
    #         self.shorturl = code_generator()
    #     super(Url,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        """can just template variable to object.get_short_url"""
        url_path = reverse('scode', kwargs={'shorturl': self.shorturl})#host='www', scheme='http'
        # kwargs shortcode is coming from urls.py name urlpattern
        return url_path