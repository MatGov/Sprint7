# Usa uma imagem base Python leve
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos de dependência e instala
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia o código da aplicação
COPY app.py .

# O container escuta na porta 8081
EXPOSE 8081

# Comando para rodar a aplicação quando o container iniciar
CMD ["python", "app.py"]