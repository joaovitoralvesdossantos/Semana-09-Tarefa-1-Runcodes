# Verifica se os valores é triangulo ou quadrado
def soma(triangulo):
    n1 = triangulo[0]
    n2 = triangulo[1]

    if n1 == n2:
        return "Os números que você digitou formam um quadrado." 
    else:
        return f"O perímetro do retangulo é {(n1+n2)*2} e a área {n1*n2}."
    
# Função principal
def main():

    #entrada de dados
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    
    #processamento
    triangulo = [n1, n2]
    resultado = soma(triangulo)
    
    #saida de dados
    print(resultado)

# Chama a função principal
if __name__ == '__main__':
    main()