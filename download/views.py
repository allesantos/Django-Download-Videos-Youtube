from django.shortcuts import render
from .forms import VideoDownloadForm # Importa o formulário de download de vídeos
import os # Biblioteca para manipulação de diretórios e arquivos
import yt_dlp # Biblioteca para baixar vídeos e áudios do YouTube

def baixar_video_yt_dlp(url, destino="media/videos"):
    """
    Função para baixar vídeos do YouTube usando a biblioteca yt_dlp.

    Parâmetros:
        url (str): URL do vídeo no YouTube.
        destino (str): Caminho do diretório onde o vídeo será salvo.

    Retorna:
        str: Título do vídeo baixado.
    """
    # Verifica se o diretório de destino existe; se não, cria o diretório
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Configurações para o yt_dlp
    ydl_opts = {
          'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),  # Caminho e nome do arquivo
            'format': 'bestvideo+bestaudio/best',  # Baixa a melhor qualidade disponível
            'merge_output_format': 'mp4',  # Garante o formato final em MP4
        'noplaylist': True,  # Baixar apenas o vídeo, não uma playlist
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # Converte o vídeo para MP4
            }
        ],
        'http_headers': {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    }

    # Realiza o download do vídeo
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return info.get('title', 'video')  # Retorna o título do vídeo baixado
    

def baixar_audio_yt_dlp(url, destino="media/audios"):
    """
    Função para baixar apenas o áudio de vídeos do YouTube usando a biblioteca yt_dlp.

    Parâmetros:
        url (str): URL do vídeo no YouTube.
        destino (str): Caminho do diretório onde o áudio será salvo.

    Retorna:
        str: Título do áudio baixado.
    """
    # Verifica se o diretório de destino existe; se não, cria o diretório
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Configurações para o yt_dlp
    ydl_opts = {
        'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),  # Caminho e nome do arquivo
        'format': 'bestaudio/best',  # Baixa a melhor qualidade de áudio disponível
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # Converte o áudio para MP3
                'preferredquality': '192',  # Define a qualidade do áudio
            },
        ],
        'noplaylist': True,  # Baixar apenas o áudio do vídeo, não uma playlist
        'quiet': False,  # Exibe logs detalhados no terminal
        'http_headers': {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36"
        },
        'overwrites': True  # Sobrescreve arquivos existentes
    }

    try:

        # Realiza o download do áudio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return info.get('title', 'audio')  # Retorna o título do áudio baixado
    except Exception as e:
        print(f"Erro ao baixar áudio: {e}")
        raise

def download_video(request):
    """
    View para processar o formulário e realizar o download de vídeos ou áudios.

    Parâmetros:
        request (HttpRequest): Objeto que contém os dados da requisição.

    Retorna:
        HttpResponse: Renderiza o template com o formulário e mensagens de feedback.
    """
    message = None # Mensagem de feedback para o usuário
    message_class = None # Classe CSS para estilizar a mensagem

    if request.method == 'POST': # Verifica se o método da requisição é POST
        form = VideoDownloadForm(request.POST) # Instancia o formulário com os dados enviados

        if form.is_valid(): # Valida os dados do formulário
            url = form.cleaned_data['url'] # URL do vídeo fornecida pelo usuário
            tipo_download = form.cleaned_data['tipo_download'] # Tipo de download (vídeo ou áudio)

            try:
                if tipo_download == 'video': # Se o usuário escolheu "vídeo"
                    video_title = baixar_video_yt_dlp(url)
                    message = f"Vídeo '{video_title}' baixado com sucesso!"
                    message_class = "success"

                elif tipo_download == 'audio': # Se o usuário escolheu "áudio"
                    audio_title = baixar_audio_yt_dlp(url)
                    message = f"Áudio '{audio_title}' baixado com sucesso!"
                    message_class = "success"

            except Exception as e: # Caso ocorra algum erro no download
                message = f"Ocorreu um erro: {e}"
                message_class = "error"
    else:
        form = VideoDownloadForm() # Instancia o formulário vazio para requisições GET
        
    # Renderiza o template com o formulário e as mensagens de feedback    
    return render(request, 'download_video.html', {'form': form, 'message': message, 'message_class': message_class})


