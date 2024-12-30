from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
# Create your views here.
class HelloWorld(View):
    def get(self,request):
        return HttpResponse('<h1>This response is class based view</h1>')

class TemplateCBV(TemplateView):
    template_name='testapp/results.html'

class TemplateCBV2(TemplateView):
    template_name='testapp/results2.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['Name']="Sunny"
        context['Marks']=98
        context['Subject']='Python'
        return context