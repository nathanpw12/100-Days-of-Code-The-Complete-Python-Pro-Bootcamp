bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi)) # 30

print(round(bmi)) # 31

print(round(bmi, 2)) # 30.85

###### Operadores de Atribuição ######

# Atribui a operação da direita ao número da esquerda

# +=
#
# -=
#
# *=
#
# /=

pontos = 0

pontos += 1 # pontos + 1 = 1
print(pontos)

pontos -= 1 # pontos - 1 = 0
print(pontos)

pontos *= 1 # pontos * 1 = 0
print(pontos)

pontos /= 1 # pontos / 1 = 0.0
print(pontos)


###### f-strings ######
# Permite usar vários tipos de dados em uma string ao declarar a string com um f logo atrás
# das aspas

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

# PEMDAS
