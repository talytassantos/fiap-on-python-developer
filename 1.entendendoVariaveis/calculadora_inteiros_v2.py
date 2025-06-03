def main():
    print("Bem-vindo à calculadora de inteiros!")
    try:
        primeiro_valor = int(input("Por favor, insira o primeiro valor: "))
        segundo_valor = int(input("Por favor, insira o segundo valor: "))
    except ValueError:
        print("Por favor, insira apenas números inteiros.")
        return

    soma = primeiro_valor + segundo_valor
    print(f"A soma entre os valores é {soma}")

    subtracao = primeiro_valor - segundo_valor
    print(f"A subtração entre os valores é {subtracao}")

    multiplicacao = primeiro_valor * segundo_valor
    print(f"A multiplicação entre os valores é {multiplicacao}")

    try:
        divisao = primeiro_valor / segundo_valor
        print(f"A divisão entre os valores é {divisao}")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")

if __name__ == "__main__":
    main()