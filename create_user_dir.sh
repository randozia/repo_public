#!/bin/bash

# Diretórios base
BASE_DIR="/departamentos"

# Departamentos e grupos
declare -A departamentos=(
  ["TI"]="grupo_ti"
  ["RH"]="grupo_rh"
  ["Seguranca"]="grupo_seguranca"
)

# Criação dos diretórios e grupos
echo "Criando diretórios e grupos..."

mkdir -p "$BASE_DIR"

for depto in "${!departamentos[@]}"; do
  dir="$BASE_DIR/$depto"
  grupo="${departamentos[$depto]}"

  # Cria grupo se não existir
  if ! getent group "$grupo" > /dev/null; then
    groupadd "$grupo"
    echo "Grupo $grupo criado."
  else
    echo "Grupo $grupo já existe."
  fi

  # Cria diretório e aplica permissões
  mkdir -p "$dir"
  chown root:"$grupo" "$dir"
  chmod 770 "$dir"
  echo "Diretório $dir criado e configurado para o grupo $grupo."
done

echo ""
echo "Agora vamos criar os usuários para cada departamento."

# Loop para criação de usuários
for depto in "${!departamentos[@]}"; do
  grupo="${departamentos[$depto]}"
  echo ""
  echo "Digite os nomes dos usuários para o departamento $depto (separados por espaço):"
  read -r -a usuarios

  for user in "${usuarios[@]}"; do
    if id "$user" &>/dev/null; then
      echo "Usuário $user já existe. Adicionando ao grupo $grupo."
      usermod -aG "$grupo" "$user"
    else
      useradd -m -G "$grupo" "$user"
      echo "Usuário $user criado e adicionado ao grupo $grupo."
      # Define senha temporária (pode ser ajustado)
      echo "$user:Senha123" | chpasswd
    fi
  done
done

echo ""
echo "Todos os usuários e diretórios foram criados com sucesso."
