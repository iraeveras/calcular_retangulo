
def calculadora(lista):
    return f"{lista}"



lista = list()
soma = 0

while True:
    entrada = input("O que voce deseja fazer, operação de SOMA, MULT, DIVISAO, SUBTRAÇÃO OU SAIR? ")
    if entrada == "sair":
        break
    if entrada == "soma":
        while True:
            num = float(input("Digite um numero: "))            
            lista.append(num)
            opcao =  input("Deseja continuar ou parar? ")
            if opcao == "continuar":
                continue
            elif opcao == "parar":
                for numero in lista:
                    soma += numero
                    print(f"{calculadora(soma)}")
                break

# print(lista)





