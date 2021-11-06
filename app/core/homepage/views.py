import json
import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from weasyprint import HTML, CSS

from core.erp.forms import SaleForm, ClientForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Sale, Product, DetSale, Client

from django.views.generic import TemplateView, CreateView


class IndexView(TemplateView):
    template_name = 'index.html'

class NosotrosView(TemplateView):
    template_name = 'nosotros.html'

class AnunciosView(TemplateView):
    template_name = 'anuncios.html'

class ContactoView(TemplateView):
    template_name = 'contacto.html'

class ProcesosView(TemplateView):
    template_name = 'procesos.html'

class ProductosView(TemplateView):
    template_name = 'productos.html'
