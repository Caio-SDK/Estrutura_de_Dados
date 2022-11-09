from pilha import Pilha
import sys


# Iniciando uma pilha
pilha = Pilha()


# Classe Menu
class Menu:

    # Método estático para o menu principal
    @staticmethod
    def menu_principal():

        # Enquant...
        while True:

            # Exibir todas as opções que o usuário pode escolher
            print("""
[ 1 ] = Adicionar algo da pilha
[ 2 ] = Remover algo da pilha
[ 3 ] = Visualizar o estado atual da pilha
[ 4 ] = Sair do programa""")

            try:

                # Seleção da opção
                opcao_desejada = int(input("Digite sua opção: "))

                if opcao_desejada == 1:

                    # Adiciona o que for digitado no input a pilha 
                    item = input("Digite o que você deseja adicionar a pilha: ")
                    pilha.add(item)
                
                elif opcao_desejada == 2:

                    # Remove algo da pilha
                    pilha.pop()

                elif opcao_desejada == 3:

                    # Exibir todos os itens dentro da pilha
                    print("\n" + "=-"*20 + "\n")
                    print(pilha)
                    print("=-"*20)
                
                elif opcao_desejada == 4:

                    # Sai do programa
                    raise KeyboardInterrupt

                else:

                    print("Opcao desejada inválida.")
            
            except KeyboardInterrupt:

                print("Obrigado pelo teste.")
                sys.exit()

            except:

                print("Digite um número inteiro válida.")
            