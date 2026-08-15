receita = ["farinha", "açúcar", "ovos", "leite", "fermento", "manteiga"]

ingredientes_pessoa1 = {"farinha", "ovos", "manteiga"}
ingredientes_pessoa2 = {"açúcar", "leite"}

# União dos ingredientes que as duas pessoas já têm
ja_tem = ingredientes_pessoa1 | ingredientes_pessoa2

# Diferença entre a receita e o que já têm = o que falta comprar
falta_comprar = set(receita) - ja_tem

print("Ingredientes que ainda faltam comprar:", falta_comprar)