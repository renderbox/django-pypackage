from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from pypackage.models import Package, Version

class IndexView(TemplateView):
    template_name = "pypackage/index.html"


class PackageView(ListView):
    model = Package


class VersionView(DetailView):
    model = Package

    