# Use uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copie o arquivo de dependências e instale-as
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copie o restante dos arquivos
COPY . .

# Exponha a porta que o Flask usa
EXPOSE 5000

# Execute o aplicativo
CMD ["python", "app.py"]
