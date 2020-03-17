from django.views.generic import TemplateView
from.models import Features, Services, Publicacoes




# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['features'] = Features.objects.all()
        context['services'] = Services.objects.all()
        context['publicacao'] = reversed(Publicacoes.objects.all())        
        return context
    

class SingleView(TemplateView):
    template_name = 'single_page.html'

    def get_context_data(self, pk, **kwargs):
        context = super(SingleView, self).get_context_data(**kwargs)
        context['publicacao'] = Publicacoes.objects.get(id=pk)
        return context

