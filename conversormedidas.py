class Medidas:
   def __init__(self) -> None:
       pass

def metros_para_centimetros(metros):
    return metros * 100

def centimetros_para_metros(centimetros):
    return centimetros / 100

def main():
    print("Escolha a opção:")
    print("1. Converter de Metros para Centímetros")
    print("2. Converter de Centímetros para Metros")
    opcao = input("Digite 1 ou 2: ")

    if opcao == "1":
        metros = float(input("Digite a medida em Metros: "))
        print("Medida em Centímetros:", metros_para_centimetros(metros))
    elif opcao == "2":
        centimetros = float(input("Digite a medida em Centímetros: "))
        print("Medida em Metros:", centimetros_para_metros(centimetros))
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")
