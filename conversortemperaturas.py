class Temperatura:
   def __init__(self) -> None:
       pass


def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Escolha a opção:")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")
    opcao = input("Digite 1 ou 2: ")

    if opcao == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        print("Temperatura em Fahrenheit:", celsius_para_fahrenheit(celsius))
    elif opcao == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print("Temperatura em Celsius:", fahrenheit_para_celsius(fahrenheit))
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")
