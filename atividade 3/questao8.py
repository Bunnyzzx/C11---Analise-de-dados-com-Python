produtos = []

for i in range(3):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    quantidade = int(input(f"Digite a quantidade em estoque do produto {i+1}: "))
    
    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)

print("--- Resumo do estoque ---")
for produto in produtos:
    valor_total = produto["preco"] * produto["quantidade"]
    print(f"Produto: {produto['nome']} | Valor total em estoque: {valor_total:.2f}")