# Base
def divisaointeira(numero):
    n = numero
    resto = n % 5  

    if resto == 0:
        return f"O resultado da equação é: {(9 * n) + 7}"
    
    elif resto == 1:
        if n % 2 == 0:
            return "Esse número é par"
        else:
            return "Esse número é ímpar"
        
    elif resto == 2:
        return f"O resultado da equação é: {(5 * (n ** 2)) - (3 * n) + 42}"
    
    elif resto == 3:
        return f"A divisão inteira do valor é: {n // 10}"
    
    elif resto == 4:
        return f"O quadrado do valor é: {n * n}"

# Função principal
def main():

    #entrada de dados
    n = int(input("Digite um número: "))
    
    #processamento
    resultado = divisaointeira(n)

    #saida de dados
    print(resultado)

# Chama a função principal
if __name__ == '__main__':
    main()