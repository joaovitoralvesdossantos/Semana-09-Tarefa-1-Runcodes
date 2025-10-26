# determina se é o 2 ou 3 número que possui diferença ao 1 e calcula a diferença dos numeros  
def testes(numeros):
    n1 = numeros[0]
    n2 = numeros[1]
    n3 = numeros[2]

    if n1 > n2:
        diferenca_n2 = n1 - n2
    else:
        diferenca_n2 = n2 - n1
    if n1 > n3:
        diferenca_n3 = n1 - n3
    else:
        diferenca_n3 = n3 - n1

    if diferenca_n2 <= diferenca_n3:
        return diferenca_n2
    else:
        return diferenca_n3

# Função principal
def main():

    #entrada de dados
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    
    #processamento
    numeros = [n1, n2, n3]
    resultado = testes(numeros)
    
    #saida de dados
    print(f"O valor da diferença é: {resultado}")

# Chama a função principal
if __name__ == '__main__':
    main()