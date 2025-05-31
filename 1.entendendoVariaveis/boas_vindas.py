from datetime import datetime

nome = input("Por favor, informe o seu nome: ").strip()

if not nome:
    print("Você não informou um nome. Tente novamente.")
else:
    hora = datetime.now().hour
    if hora < 12:
        saudacao = "Bom dia"
    elif hora < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"
    print(f"{saudacao}, {nome}! Seja bem-vindo(a) ao programa.")