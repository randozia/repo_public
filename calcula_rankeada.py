def calcular_rank(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif 10 < vitorias <= 20:
        nivel = "Bronze"
    elif 20 < vitorias <= 50:
        nivel = "Prata"
    elif 50 < vitorias <= 80:
        nivel = "Ouro"
    elif 80 < vitorias <= 90:
        nivel = "Diamante"
    elif 90 < vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo_vitorias, nivel

# Exemplo de uso:
vitorias = 75
derrotas = 25

saldo, nivel = calcular_rank(vitorias, derrotas)
print(f"O Herói tem de saldo de **{saldo}** está no nível de **{nivel}**")
