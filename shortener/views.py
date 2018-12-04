from django.shortcuts import render,get_object_or_404,redirect,reverse,HttpResponseRedirect,Http404,HttpResponsePermanentRedirect
from django.http import HttpResponse
from .models import Url
from django.views import View


class Home(View):
    def get(self,request,*args,**kwargs):
        return render(request,'shortener/index.html',{})

    def post(self,request,*args,**kwargs):
        url = request.POST.get("url")
        obj,created = Url.objects.get_or_create(url=url)

        context = {
            'object':obj,
            'created':created,
        }
        return render(request,'shortener/success.html',context)


#Deveria
# #Pega o shortcode e redireciona pra sua respectiva url com base no get shorturl no models
class URLRedirectView(View): #class based views, must specify method
    def get(self, request, shorturl=None, *args, **kwargs):
        qs = Url.objects.filter(shorturl__iexact=shorturl)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        # obj = get_object_or_404(KirrURL, shortcode=shortcode)
        # print (ClickEvent.objects.create_event(obj))
        return HttpResponsePermanentRedirect(obj.url)