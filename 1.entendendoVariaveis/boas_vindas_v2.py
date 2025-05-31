from datetime import datetime

def obter_nome():
    while True:
        nome = input("Por favor, informe o seu nome: ").strip()
        if nome:
            return nome
        print("Você não informou um nome. Tente novamente.\n")

def obter_saudacao():
    hora = datetime.now().hour
    if hora < 12:
        return "Bom dia"
    elif hora < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

def main():
    nome = obter_nome()
    saudacao = obter_saudacao()
    print(f"{saudacao}, {nome}! Seja bem-vindo(a) ao programa.")

if __name__ == "__main__":
    main()