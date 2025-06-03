def calcular_velocidade_media():
    print("Simulador de computador de bordo")
    try:
        distancia = float(input("Informe a distância percorrida em km: "))
        tempo = float(input("Informe o tempo da viagem em horas: "))
        if distancia <= 0 or tempo <= 0:
            print("Distância e tempo devem ser valores positivos.")
            return
        velocidade_media = distancia / tempo
        print(
            f"A velocidade média da viagem foi de {velocidade_media:.2f} km/h")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")


if __name__ == "__main__":
    calcular_velocidade_media()
