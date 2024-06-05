def sair():
    print("encerrando o programa...")

def menu_principal():
    while True:
        print("\n*calculadora de conversão de unidades*")
        print("1. conversor de medidas")
        print("2. conversor de temperaturas")
        print("3.sair")
        opção = input("digite a opção desejada: ")
        if opção == "1":
            from conversormedidas import Medidas
        elif opção == "2":
            from conversortemperaturas import Temperatura
        elif opção == "3":
            sair()
            break
        else:
            print("opção inválida. tente novamente.")
menu_principal() 

