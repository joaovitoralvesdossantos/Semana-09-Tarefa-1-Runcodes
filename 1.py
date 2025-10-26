# Calcula se são valores igual, diferentes ou possui dois iguais e um diferente.
def testes(numeros):
    n1 = numeros[0]
    n2 = numeros[1]
    n3 = numeros[2]
    if n1 == n2 and n2 == n3:
        return "Todos os valores são iguais"
    elif n1 != n2 and n2 != n3 and n1 != n3:
        return "Todos os valores são diferentes"
    else:
        return "Existem dois valores iguais e um diferente"

# Função principal
def main():

    #entrada de dados
    n1 = int(input("Digite o valor do primeiro número: "))
    n2 = int(input("Digite o valor do segundo número: "))
    n3 = int(input("Digite o valor do terceiro número: "))
    
    #processamento
    
    numeros = [n1, n2, n3]
    resultado = testes(numeros)
    
    #saida de dados
    print(resultado)

# Chama a função principal
if __name__ == '__main__':
    main()