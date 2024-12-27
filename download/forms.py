from django import forms # Importa o módulo de formulários do Django

"""
    Formulário para entrada de dados necessários para download de vídeos ou áudios.
"""

class VideoDownloadForm(forms.Form):
    # Campo para o usuário inserir a URL do vídeo
    url = forms.URLField(
        label='URL do Vídeo', # Rótulo exibido no formulário

        # Texto de sugestão dentro do campo e Classe CSS para estilização
        widget=forms.TextInput(attrs={'placeholder': 'Cole aqui a URL do vídeo', 'class': 'form-control'})
    )

    # Campo para o usuário selecionar o tipo de download (vídeo ou áudio)
    tipo_download = forms.ChoiceField(
        choices=[('video', 'Vídeo'), ('audio', 'Áudio')], # Opções disponíveis no menu suspenso
        label='Tipo de Download', # Rótulo exibido no formulário
        widget=forms.Select(attrs={'class': 'form-control'}), # Classe CSS para estilização
        initial='video' # Valor padrão selecionado (vídeo)
    )

