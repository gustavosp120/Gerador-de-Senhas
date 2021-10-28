# Maiúsculas e minuscilas
# Simbolos e Espaços

"""
Security = chave
5eCur1ty = senha 

hex

1 = 1
2 = 2
até 9 = 9
10 = a 
11 = b
12 = c 
13 = D
14 = e
15 = f 
16 = g

...

"""


chave = input("Digite a base da sua senha: ")


senha = ""
for letra in chave:
    if letra in "Aa":
        senha = senha + "6"
    elif letra in "Bb":
        senha = senha + "@"
    elif letra in "Cc":
        senha = senha + "3"
    elif letra in "Dd":
        senha = senha + "7"
    elif letra in "Ee":
        senha = senha + "1"
    elif letra in "Ff":
        senha = senha + "&"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Ss":
        senha = senha + "%"
    elif letra in "Mm":
        senha = senha + "$"
    else:
        senha = senha + letra
print(senha)
