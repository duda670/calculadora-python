def calcular(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b == 0:
            return "Erro: divisão por zero"
        return a / b
    else:
        return "Operação inválida"


def main():
    print("=== Calculadora ===")
    while True:
        try:
            a = float(input("Primeiro número: "))
            operacao = input("Operação (+, -, *, /): ")
            b = float(input("Segundo número: "))
        except ValueError:
            print("Digite apenas números válidos.\n")
            continue

        print("Resultado:", calcular(a, b, operacao))

        de_novo = input("\nQuer calcular de novo? (s/n): ").lower()
        if de_novo != "s":
            print("Até mais!")
            break


main()