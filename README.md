# YouTube Downloader com Django

Este é um projeto desenvolvido em Django feito para carregar uma interface onde o usuário poderá fazer download de vídeos e audios do Youtube.

## Índice
- [Descrição](#Descrição)
- [Tecnologias Utilizadas](#Tecnologias)
- [Pré-requisitos](#Pré-requisitos)
- [Instalação](#Instalação)
- [Uso](#Uso)
- [Contribuição](#Contribuição)
- [Licença](#Licença)


## Descrição
Este projeto oferece uma interface web simples para os usuários baixarem vídeos ou extraírem o áudio de vídeos do YouTube. O usuário insere a URL de um vídeo do YouTube e pode escolher entre fazer o download do vídeo completo ou apenas o áudio.



## Tecnologias
-  __Python 3__
  
-  __Django__
  
-  __Biblioteca pytube__ para manipulação e download de vídeos do YouTube

-  __HTML/CSS/JavaScript__ para a interface do usuário



## Pré-requisitos
Antes de começar, você precisará ter as seguintes ferramentas instaladas:
-  __Python 3.8__ ou superior
-  Virtualenv (opcional, mas recomendado)
-  __Git__
  
Além disso, recomenda-se usar um ambiente virtual Python para gerenciar dependências.


## Instalação
Siga os passos abaixo para configurar o projeto:

1. Clone o repositório para sua máquina local:

    ```
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie e ative um ambiente virtual:

    ```
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências do projeto:

    ```
    pip install -r requirements.txt
    ```

4. Inicie o servidor de desenvolvimento:

    ```
    python manage.py runserver
    ```

5. Acesse o sistema em http://127.0.0.1:8000/ no seu navegador.


 
## Uso

1. Acesse o sistema pelo navegador através do endereço http://127.0.0.1:8000/.

2. Insira a URL do vídeo do YouTube no campo de texto fornecido.

3. Escolha entre baixar o vídeo ou apenas o áudio.

4. Clique no botão para iniciar o download.


 
## Contribuição
Sinta-se à vontade para contribuir com este projeto. Siga estas etapas:

1. Faça um fork do repositório.

2. Crie uma nova branch para sua feature/bugfix:

    ```
    git checkout -b minha-feature
    ```

3. Envie suas alterações:

    ```
    git push origin minha-feature
    ```

4. Abra um Pull Request neste repositório.

## Licença


Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.
