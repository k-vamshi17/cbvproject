from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
class HelloWorld(View):
    def get(self,request):
        return HttpResponse('<h1>This response is class based view</h1>')