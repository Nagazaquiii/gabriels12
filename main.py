from conversortemperaturas import ConversorTemperatura
from conversormedidas import ConversorMedidas


print("Sou o gabriel Nunes gostoso e vou te ajudar a resolver seus cálculos\n")
print("1. converter temperatura celcius para fahrenheit\n2. converter temperatura fahrenheit para celcius\n3. converter medidas centimetros para metros\n4. converter medidas metros para centimetos")

op = (input("Digite a opção desejada:"))
    
    
if op == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = ConversorTemperatura.celsius_to_fahrenheit(celsius)
        print(f"{celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit.")
elif op == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = ConversorTemperatura.fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit é igual a {celsius} graus Celsius.")
elif op == "3":
      conversor = float(input("Digite a quantidade em centímetros que deseja converter para metros:\n")) / 100
      print(f"O valor convertido é {conversor} metros.")
elif op == "4":
       conversor = float(input("Digite a quantidade em metros que deseja converter para centímetros:\n")) * 100
       print(f"O valor convertido é {conversor} centímetros.")
else:
        print("Escolha inválida.")