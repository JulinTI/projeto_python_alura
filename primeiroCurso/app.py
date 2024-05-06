import os 
import time

restaurantes = [{'nome': 'Cantina Mineira', 'categoria': 'Comida Mineira', 'ativo': True}, {'nome': 'Sushi Japa', 'categoria': 'Comida Japonesa', 'ativo': False}]

def exibir_nome():
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair')

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu()

def finalizar_app():
    os.system('cls')
    print('Finalizando app...')
    time.sleep(2)

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurate {nome_do_restaurante} foi cadastrado com sucesso!\n')
    opcao = input('Deseja cadastrar um novo restaurate? Sim ou Nao ')
    opcao_fornecida = opcao.capitalize()
    
    if opcao_fornecida != 'Sim':
        print('Voltando ao menu principal ')
        time.sleep(2)
        main()
    else:
        cadastrar_restaurante()



def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def alternando_estado_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')

    voltar_ao_menu()


def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status \n')
    for restaurante in restaurantes:
        nome_cadastrado = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_cadastrado.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternando_estado_restaurante()
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