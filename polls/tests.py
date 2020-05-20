from django.test import TestCase

# Create your tests here.

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Pergunta


class PerguntaModelTests(TestCase):

    def teste_publicado_recentemente_with_pergunta_futura(self):
    
        time = timezone.now() + datetime.timedelta(days=30)
        pergunta_futura = Pergunta(data_publicacao=time)
        self.assertIs(pergunta_futura.publicado_recentemente(), False)