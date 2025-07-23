# STRINGS

nome = "Joel Teixeira da Cunha"

print(nome.upper())
print(nome.lower())
print(nome.title())

# Retira os espaços

texto = "   Olá mundo!!!   "

print(texto)
print(texto.strip()+".")
print(texto.rstrip()+".")
print(texto.lstrip()+".")

# Centralização

menu = "Python"
print(menu.center(20))
print(menu.center(20, "-"))

# Separar as letras da palavra

print("-". join(menu))