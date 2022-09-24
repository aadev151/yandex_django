from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'portfolio/index.html'


def not_found_view(request, exception):
    return render(request, 'portfolio/404.html')
