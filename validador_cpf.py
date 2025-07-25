import os

def mostrar_menu():
    os.system('clear')
    print(
        '''
        
        ██╗░░░██╗░█████╗░██╗░░░░░██╗██████╗░░█████╗░██████╗░░█████╗░██████╗░  ░█████╗░██████╗░███████╗
        ██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔════╝
        ╚██╗░██╔╝███████║██║░░░░░██║██║░░██║███████║██║░░██║██║░░██║██████╔╝  ██║░░╚═╝██████╔╝█████╗░░
        ░╚████╔╝░██╔══██║██║░░░░░██║██║░░██║██╔══██║██║░░██║██║░░██║██╔══██╗  ██║░░██╗██╔═══╝░██╔══╝░░
        ░░╚██╔╝░░██║░░██║███████╗██║██████╔╝██║░░██║██████╔╝╚█████╔╝██║░░██║  ╚█████╔╝██║░░░░░██║░░░░░
        ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░░░░╚═╝░░░░░

        
        Author: Rodrigo Gutierrez Andozia [rodrigo.andozia@gmail.com] ®
        Versão: 1.0
        
        
        1. Validar CPF
        2. Finalizar programa

        '''
    )

def ler_cpf():
    cpf = input('\tDigite o CPF para validar [xxx.xxx.xxx-xx]: ')
    return cpf

def transforma_cpf(cpf):
    cpf_sem_ponto = cpf.replace('.','')
    cpf_sem_traco = cpf_sem_ponto.replace('-','')
    cpf_numerico = cpf_sem_traco.strip()
    return cpf_numerico

def validar_primeiro_digito(cpf_somente_numeros):
    soma_total = 0
    contador = 10
    i = 0   
    while contador >= 2:
        soma_total = soma_total + (contador * int(cpf_somente_numeros[i]))
        contador -= 1
        i += 1
    if (((soma_total*10)%11) > 9):
        digito_validador_1 = 0
    else:
        digito_validador_1 = ((soma_total*10)%11)
    return digito_validador_1

def validar_segundo_digito(cpf_digito1_validado):
    soma_total = 0
    contador = 11
    i = 0   
    while contador >= 2:
        soma_total = soma_total + (contador * int(cpf_digito1_validado[i]))
        contador -= 1
        i += 1
    if (((soma_total*10)%11) > 9):
        digito_validador_2 = 0
    else:
        digito_validador_2 = ((soma_total*10)%11)
    return digito_validador_2

def validar_cpf(cpf):
    cpf_somente_numeros = transforma_cpf(cpf)
    cpf_digito1_validado = cpf_somente_numeros[0:9]+str((validar_primeiro_digito(cpf_somente_numeros)))
    cpf_digito2_validado = cpf_digito1_validado + str((validar_segundo_digito(cpf_digito1_validado)))
    if cpf_somente_numeros == cpf_digito2_validado:
        mensagem = f'\tCPF válidado com sucesso ✔'
    else:
        mensagem = f'\tCPF é inválido ✘'
    return mensagem
 
def main():
    mostrar_menu()
    condicional = int(input('\tDigite a opção desejada: '))
    while condicional == 1:
        cpf = ler_cpf()
        print(validar_cpf(cpf))
        condicional = int(input('\n\tDigite a opção desejada: '))
    print(
        '''
        Obrigado por utilizar o validador de CPF.
        
        '''
    )
    
if __name__ == '__main__':
    main()