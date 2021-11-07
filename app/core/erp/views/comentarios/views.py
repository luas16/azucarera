from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import ComentaryForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Coments


class ComentariosCreateView(CreateView):
    model = Coments
    form_class = ComentaryForm
    template_name = 'Comentarios.html'
    success_url = reverse_lazy('index')

    @method_decorator(csrf_exempt)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Comentario'
        return context
