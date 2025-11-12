# função para a calculadora

def calculadora(num1, num2, operacao):
    #verifica qual operação o usuário deseja realizar
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        #verifica se o segundo número é diferente de zero para evitar divisão por zero
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

#define os valores para teste
num1 = 5
num2 = 5
operacao = 'subtracao'

#chama a função calculadora com os valores definidos
resultado = calculadora(num1, num2, operacao)

#exibe o resultado da operação para o usuário
print(f"O resultado da operação {operacao} dos números {num1} e {num2} é: {resultado}")