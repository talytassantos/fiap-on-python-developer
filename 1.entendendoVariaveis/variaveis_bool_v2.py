def demonstrar_variaveis_bool():
    print("Demonstração de variáveis booleanas em Python\n")

    exemplos = [
        ("Valor inicial", False),
        ("Valor alterado", True),
        ("1 > 2", 1 > 2),
        ("1 < 2", 1 < 2),
        ("1 >= 2", 1 >= 2),
        ("1 <= 2", 1 <= 2),
        ("1 == 2", 1 == 2),
        ("1 != 2", 1 != 2),
        ("bool(0)", bool(0)),
        ("bool(15)", bool(15)),
    ]

    for descricao, valor in exemplos:
        print(f"{descricao}: {valor}")


if __name__ == "__main__":
    demonstrar_variaveis_bool()
