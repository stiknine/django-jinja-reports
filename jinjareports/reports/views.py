from django.views import generic
from django.urls import reverse_lazy


class IndexView(generic.TemplateView):
    """Index page view."""

    template_name = 'index.html'


class DTLIndexView(generic.TemplateView):
    """Django template Index page view."""

    template_name = 'dtl_index.html'
