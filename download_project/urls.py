from django.contrib import admin
from django.urls import path, include # Funções para roteamento de URLs
from django.conf import settings # Importa as configurações do projeto
from django.conf.urls.static import static # Função para servir arquivos estáticos e de mídia

# Definição das rotas do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('download.urls')),  # Inclui as rotas definidas no aplicativo 'download'
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG: # Verifica se o modo de depuração está ativado

    # Adiciona uma rota para servir arquivos de mídia (ex.: vídeos ou áudios) do diretório MEDIA_ROOT
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
