from desafio_operacao_bancaria import valor_deposito

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")


print()

# RANGE, início, fim, step
for numero in range(0, 51, 5):
    print(numero, end=" - ")

descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:
if cupom == "DESCONTO10":
   valor_produto = preco - (preco * 10/100)
   print(valor_produto)

elif cupom == "DESCONTO20":
    valor_produto = preco - (preco * 20 / 100)
    print(valor_produto)

elif cupom == "SEM_DESCONTO":
    print(preco)
