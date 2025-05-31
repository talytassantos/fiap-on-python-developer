# criando uma lista
lista = [12, 15.5, "texto"]
print(lista)

# inserindo novos elementos no fim da lista
lista.append("Teste de inserção")
print(lista)

# mostrando elemento pelo indice
print(lista[0])
print(lista[0:3])

# Exibindo com o loop
for valor in lista:
    print(valor)

# remove o ultimo elemento da lista
lista.pop()
print(lista)
lista.remove(12)
print(lista)

# tamanho da lista
print(len(lista))
