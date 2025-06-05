from datetime import datetime


def cadastrar_doador():
    print("Cadastro de doadores de sangue")
    try:
        nome = input("Por favor, digite seu nome completo: ")
        peso = float(input("Por favor, digite seu peso em quilos: "))
        altura = int(input("Por favor, digite sua altura em centímetros: "))
        nascimento = int(input("Por favor, digite seu ano de nascimento: "))
        ano_atual = datetime.now().year
        idade = ano_atual - nascimento

        if peso <= 0 or altura <= 0 or nascimento <= 1900 or idade < 0:
            print(
                "Por favor, insira valores válidos para peso, altura e ano de nascimento.")
            return

        tem_peso_minimo = peso > 50
        tem_idade_minima = idade >= 16

        print("\n--- Dados do Doador ---")
        print(f"NOME: {nome.upper()}")
        print(f"PESO: {peso:.1f} kg")
        print(f"ALTURA: {altura} cm")
        print(f"IDADE: {idade} anos")
        print(
            f"TEM PESO MÍNIMO PARA DOAR: {'Sim' if tem_peso_minimo else 'Não'}")
        print(
            f"TEM IDADE MÍNIMA PARA DOAR: {'Sim' if tem_idade_minima else 'Não'}")
    except ValueError:
        print("Entrada inválida. Por favor, insira valores numéricos corretos.")


if __name__ == "__main__":
    cadastrar_doador()
