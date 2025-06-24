#!/bin/bash

# Verifica se o script está sendo executado como root
if [ "$EUID" -ne 0 ]; then
  echo "Por favor, execute como root (use sudo)"
  exit 1
fi

echo "Atualizando os pacotes..."
apt update -y && apt upgrade -y

echo "Instalando o Apache2..."
apt install apache2 -y

echo "Ativando e iniciando o serviço Apache2..."
systemctl enable apache2
systemctl start apache2

echo "Verificando o status do Apache2..."
systemctl status apache2

echo "Instalação do Apache2 concluída com sucesso!"