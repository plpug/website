from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    """
    Home page
    """
    template_name = 'index.html'


