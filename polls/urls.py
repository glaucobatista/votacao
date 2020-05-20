from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetalheView.as_view(), name='detalhe'),
    path('<int:pk>/resultados/', views.ResultadosView.as_view(), name='resultados'),
    path('<int:pergunta_id>/vote/', views.voto, name='voto'),
]