from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .models import Features, Services, Publicacoes, Funcionario, Clientes, Counter
from django.contrib import messages



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['features'] = Features.objects.all()
        context['services'] = Services.objects.all()
        context['publicacao'] = reversed(Publicacoes.objects.all())
        context['funcionario'] = Funcionario.objects.all()
        context['clientes'] = Clientes.objects.all()
        context['counter'] = Counter.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar mensagem!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
    

class SingleView(TemplateView):
    template_name = 'single_page.html'

    def get_context_data(self, pk, **kwargs):
        context = super(SingleView, self).get_context_data(**kwargs)
        context['publicacao'] = Publicacoes.objects.get(id=pk)
        return context
