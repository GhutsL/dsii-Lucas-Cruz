import math

def calc():
    print("Calculadora - Feita por Lucas Matias Cruz")
    
    while True:
        print("\nMenu:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Potenciação (^)")
        print("6. Raiz Quadrada (√)")
        print("7. Pi (π)")
        print("8. Tangente (tan)")
        print("9. Cosseno (cos)")
        print("10. Seno (sin)")
        print("11. Logaritmo (log)")
        print("12. Fatorial (fatorial)")
        print("13. Sair")

        escolha = input("Digite o número presente na frente da operação desejada: ")

        if escolha == '1':  
            num1 = float(input('Informe o primeiro número: '))
            num2 = float(input('Informe o segundo número: '))
            print(f"Resultado da Adição: {num1 + num2},  Feita por Lucas Matias Cruz")

        elif escolha == '2':  
            num1 = float(input('Informe o primeiro número: '))
            num2 = float(input('Informe o segundo número: '))
            print(f"Resultado da Subtração: {num1 - num2}, Feita por Lucas Matias Cruz")

        elif escolha == '3':  
            num1 = float(input('Informe o primeiro número: '))
            num2 = float(input('Informe o segundo número: '))
            print(f"Resultado da Multiplicação: {num1 * num2}, Feita por Lucas Matias Cruz")

        elif escolha == '4':  
            num1 = float(input('Informe o primeiro número: '))
            num2 = float(input('Informe o segundo número: '))
            if num2 != 0:
                print(f"Resultado da Divisão: {num1 / num2}, Feita por Lucas Matias Cruz")
            else:
                print("Erro! Divisão por zero.")

        elif escolha == '5':  
            base = float(input('Digite a base: '))
            expoente = float(input('Digite o expoente: '))
            print(f"Resultado da Potenciação: {math.pow(base, expoente)}, Feita por Lucas Matias Cruz")

        elif escolha == '6':  
            num = float(input('Digite o número para calcular a raiz quadrada: '))
            if num >= 0:
                print(f"Resultado da Raiz Quadrada: {math.sqrt(num)}, Feita por Lucas Matias Cruz")
            else:
                print("Erro! Não é possível calcular a raiz quadrada de um número negativo.")

        elif escolha == '7': 
            print(f"Valor de Pi: {math.pi}, Feita por Igor Lucas Matias Cruz")

        elif escolha == '8':  
            angulo = float(input('Digite o ângulo em graus: '))
            radiano = math.radians(angulo)
            print(f"Resultado da Tangente: {math.tan(radiano)}, Feita por Lucas Matias Cruz")

        elif escolha == '9':  
            angulo = float(input('Digite o ângulo em graus: '))
            radiano = math.radians(angulo)
            print(f"Resultado do Cosseno: {math.cos(radiano)}, Feita por Lucas Matias Cruz")

        elif escolha == '10':  
            angulo = float(input('Digite o ângulo em graus: '))
            radiano = math.radians(angulo)
            print(f"Resultado do Seno: {math.sin(radiano)}, Feita por Lucas Matias Cruz")

        elif escolha == '11':  
            num = float(input('Digite o número para calcular o logaritmo: '))
            if num > 0:
                print(f"Resultado do Logaritmo: {math.log(num)}, Feita por Lucas Matias Cruz")
            else:
                print("Erro! O logaritmo de números negativos ou zero não é definido.")

        elif escolha == '12':  
            num = int(input('Digite um número inteiro para calcular o fatorial: '))
            if num < 0:
                print("Erro! O fatorial de um número negativo não é definido.")
            else:
                print(f"Resultado do Fatorial: {math.factorial(num)}, Feita por Lucas Matias Cruz")

        elif escolha == '13':  
            print("Obrigado por usar a calculadora.")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    calc()
