import os

restaurantes = []

def exibir_nome_app():
    print('Sabor Express \n');

def exibir_opcoes():
    print ('1. Cadastrar Restaurante');
    print ('2. Listar Restaurantes');
    print ('3. Ativar Restaurante');
    print ('4. Sair \n');

def voltar_menu():
    input('\nPressione qualquer tecla para voltar ao menu principal: ');
    main();

def exibir_subtitulo(subtitulo):
    os.system('cls')
    print(subtitulo);
    print();


def finalizar_app():
    exibir_subtitulo('Obrigado por utilizar o Sabor Express!')

def opcao_invalida():
    exibir_subtitulo('Opção inválida!');
    voltar_menu()
    

def cadastrar_restaurantes():
    exibir_subtitulo('Cadastro de novos restaurantes!');
    nome_restaurante = input('Digite o nome do restaurante: ');
    restaurantes.append(nome_restaurante);
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!');
    voltar_menu();

def listar_restaurantes():
    exibir_subtitulo('Listando todos os restaurantes!');
    for restaurante in restaurantes:
        print(f'- {restaurante}');
    voltar_menu();

def escolher_opcao():
    try:
        opção_escolhida = int(input('Escolha uma opção: '));

        if opção_escolhida == 1:
            cadastrar_restaurantes();
        elif opção_escolhida == 2:
            listar_restaurantes();
        elif opção_escolhida == 3:
            print('Ativar Restaurante');
        elif opção_escolhida == 4:
            finalizar_app();
        else:
            opcao_invalida();
    except:
        opcao_invalida();

def main():
    os.system('cls')
    exibir_nome_app();
    exibir_opcoes();
    escolher_opcao();

if __name__ == '__main__':
    main()
