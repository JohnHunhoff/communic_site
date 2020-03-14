from django.views.generic import TemplateView
from.models import Features, Services, Publicacoes


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['features'] = Features.objects.all()
        context['services'] = Services.objects.all()
        context['blog'] = Publicacoes.objects.all()
        return context
