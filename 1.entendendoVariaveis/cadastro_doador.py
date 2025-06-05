print("Cadastro de doadores de sangue")
nome = input("Por favor, digite seu nome completo: ")
peso = float(input("Por favor, digite seu peso em quilos: "))
altura = int(input("Por favor, digite sua altura em centímetros: "))
nascimento = int(input("Por favor, digite seu ano de nascimento: "))
idade = 2022 - nascimento
tem_peso_minimo = peso > 50
tem_idade_minima = idade >= 16
texto_saida = f"\tNOME: {nome.upper()}\n\tPESO: {peso} kg\n\tALTURA: {altura}cm\n\tIDADE: {idade} anos\n\tTEM PESO MÍNIMO PARA DOAR: {tem_peso_minimo}\n\tTEM IDADE MÍNIMA PARA DOAR: {tem_idade_minima}\n\t"
print(texto_saida)
