# ATIVIDADE 1
def saudacao(nome):
    print(f"olá, {nome}")

# saudacao("Julia")


# ATIVIDADE 2
def comprimento(horario):
    if horario < 12:
        print(f"Bom dia")
    elif horario < 18:
        print(f"Boa tarde")
    else:
        print(f"Boa noite")

horario = 12
comprimento(horario)


# ATIVIDADE 3
def soma(num1, num2):
    return f"Soma: {num1 + num2}"

print(soma(12,5))


# ATIVIDADE 4
def subtracao(num1, num2):
    return f"Subtração: {num2 - num1}"

print(subtracao(7,2))

def multiplicacao(num1, num2):
    return f"Multiplicação: {num1 * num2}"

print(multiplicacao(12,8))