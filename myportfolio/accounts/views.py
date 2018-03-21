from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomepageView(TemplateView):
    template_name = 'accounts/index.html'

class AboutView(TemplateView):
    template_name = 'accounts/about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class PhotoView(TemplateView):
    template_name = 'photos.html'

class PortfolioView(TemplateView):
    template_name = 'portfolio.html'