import os 
import time

restaurantes = []

def exibir_nome():
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def opcao_invalida():
    print('Opção inválida\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def finalizar_app():
    os.system('cls')
    print('Finalizando app...')
    time.sleep(2)


def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurate {nome_do_restaurante} foi cadastrado com sucesso!\n')
    opcao = input('Deseja cadastrar um novo restaurate? Sim ou Nao ')
    opcao_fornecida = opcao.capitalize()
    
    if opcao_fornecida != 'Sim':
        print('Opçao invalida\n')
        print('Voltando ao menu principal ')
        time.sleep(2)
        main()
    else:
        cadastrar_restaurante()


def listar_restaurantes():
    os.system('cls')
    print('Listando restaurantes: ')

    for restaurante in restaurantes:
        print(f'- {restaurante}\n')
        input('Digite uma tecla para voltar ao menu principal: ')
        main()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_escolhida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()