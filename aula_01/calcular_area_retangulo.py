largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

resultado = 0

if altura and largura:
    resultado = largura * altura
    print(f"A área do retângulo é: {resultado}")
else:
    print("Você precisa informar o valor da largura e altura")
