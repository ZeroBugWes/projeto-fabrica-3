produto = input("Qual o nome do produto: ")
mercado1 = input("Qual o nome do Supermercado: ")
preco1 =  float(input(f"Qual o preço do produto nesse {mercado1}: "))
mercado2 = input("Qual o nome do segundo Supermercado: ")
preco2 =  float(input(f"Qual o preço do produto nesse {mercado2}: "))
mercado3 = input("Qual o nome do terceiro Supermercado: ")
preco3 =  float(input(f"Qual o preço do produto nesse {mercado3}: "))

print("=== Resultado ===")
if preco1 > preco2 and preco1 < preco3:
    print(f"Produto: {produto}\nMais barato em: {mercado1}\n Preço Justo/nPreço: {preco1}")
elif preco2 < preco1 and preco2 < preco3:
    print(f"Produto: {produto}\nMais barato em: {mercado2}\n Preço Justo/nPreço: {preco2}")
else:
    print(f"Produto: {produto}\nMais barato em: {mercado3}\n Preço Justo/nPreço: {preco3}")