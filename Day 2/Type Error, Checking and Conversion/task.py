# len(12345) TypeError: object of type 'int' has no len()

# Pause 1

len("12345")

###### Verificar tipo de um dado ######

type("dados")

# Pause 2

print(type("Nathan")) # <class 'str'>
print(type(2)) # <class 'int'>
print(type(False)) # <class 'bool'>
print(type(12.2)) # <class 'float'>

###### Conversão de tipos de dados ######

int()
float()
str()
bool()

print(int("123") + int("321")) # 444

# Pause 3

print("Number of letters in your name: " + str(len(input("Enter your name\n"))))

# Usando Variáveis

length_name = len(input("Enter your name\n"))

print("Number of letters in your name:" + str(length_name))

