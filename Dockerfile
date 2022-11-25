# Dockerfile

# fazendo o pull da imagem oficial no Docker Hub
FROM python:3.10

# variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# instalação dos pacotes
WORKDIR /code
COPY . /code/

# atualizando o pip e instalando requerimentos
RUN pip install -U pip
RUN pip install -r requirements.txt