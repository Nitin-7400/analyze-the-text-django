from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('removepunc', views.removepunc, name='rempunc'),
    path('capitalizefirst', views.capfirst, name='capfirst'),
    path('newlineremove', views.newlineremove, name='newlineremove'),
    path('spaceremove', views.spaceremove, name='spaceremove'),
    path('charcount', views.charcount, name='charcount'),
  ]
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def removepunc(request):
    djtext = (request.GET.get('text', 'default'))
    # get the text
    print(djtext)
    #Analyze the text
    return HttpResponse('''<h1>remove punc</h1> <a href = "http://127.0.0.1:8000/">back to home</a1>''')
def capfirst(request):
    return HttpResponse('''<h1>capitalize first</h1> <a href = "http://127.0.0.1:8000/removepunc">back</a1>
     <a href = "http://127.0.0.1:8000/">back to home</a1>''')
def newlineremove(request):
    return HttpResponse('''<h1>new line remove</h1> <a href = "http://127.0.0.1:8000/capitalizefirst">back</a1>
     <a href = "http://127.0.0.1:8000/">back to home</a1>''')
def spaceremove(request):
    return HttpResponse('''<h1>space remove</h1> <a href = "http://127.0.0.1:8000/newlineremove">back</a1> 
     <a href = "http://127.0.0.1:8000/">back to home</a1>''')
def charcount(request):
    return HttpResponse('''<h1>char count</h1> <a href = "http://127.0.0.1:8000/spaceremove">back</a>
     <a href = "http://127.0.0.1:8000/">back to home</a1>''')
