from django.urls import path
from . import views

urlpatterns = [
    path('', views.download_video, name='download_video'),
]

# Quando o usuário acessa a URL raiz (''), a função 'download_video' do módulo 'views' é chamada.
# O parâmetro 'name='download_video' permite referenciar esta rota pelo nome em outras partes do projeto, como templates ou redirecionamentos.