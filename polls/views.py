
# Create your views here.
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Pergunta, Opcao


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lista_ultimas_perguntas'
    def get_queryset(self):
        return Pergunta.objects.filter(
        data_publicacao__lte=timezone.now()
        ).order_by('-data_publicacao')[:5]
        

class DetalheView(generic.DetailView):

    model = Pergunta
    template_name = 'polls/detalhe.html'


class ResultadosView(generic.DetailView):
    model = Pergunta
    template_name = 'polls/resultados.html'
    

def voto(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        opcao_selecionada = pergunta.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detalhe.html', {
            'pergunta': pergunta,
            'error_message': "Você não selecionou uma opção.",
        })
    else:
        opcao_selecionada.votos += 1
        opcao_selecionada.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:resultados', args=(pergunta_id,)))
