from functions.functions import *

# Main menu
while True:
    print("1 - Registrar usuário")
    print("2 - Reconhecimento facial")
    print("0 - Sair")

    option = int(input("Digite a opção: "))

    if option == 1:
        register_user()
    elif option == 2:
        facial_rec()
    elif option == 0:
        break
    else:
        print("Opção inválida!")
