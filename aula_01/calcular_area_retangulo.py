largura = float(input("Digite a largura da base: "))
altura = float(input("Digite a altura: "))

area = 0

if altura and largura:
    area = base * altura
    print(f"A área do retângulo é: {area}")
else:
    print("Você precisa informar o valor da largura e altura")
