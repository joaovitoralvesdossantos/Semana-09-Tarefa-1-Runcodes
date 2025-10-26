# Faz as contas dos números:
def conta(numeros):
    n1 = numeros[0]
    n2 = numeros[1]

    calc = n1 + n2 
    sub = n1 - n2 
    mult = n1 * n2 
    div = n1 / n2 

    return calc, sub, mult, div

# Função principal
def main():

    #entrada de dados
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o numero do operador: (1 = Adição, 2 = Subtração. 3 = Multiplicação, 4 = Divisão): "))

    #processamento
    numeros = [n1, n2, n3]
    resultado = conta(numeros)

    #saida de dados
    if n3 == 1:
        print(f"O resultado dos dois valores é: {resultado[0]}")
        
    elif n3 == 2:
        print(f"O resultado dos dois valores é: {resultado[1]}")
        
    elif n3 == 3:
        print(f"O resultado dos dois valores é: {resultado[2]}")
        
    elif n3 == 4:
        print(f"O resultado dos dois valores é: {resultado[3]:.2f}")


# Chama a função principal
if __name__ == '__main__':
    main()