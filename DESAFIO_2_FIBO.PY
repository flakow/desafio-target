entrada = int(input("Informe um número: "))
fibonacci = [0, 1]

while fibonacci[-1] < entrada:
    proximo_valor = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_valor)

if entrada in fibonacci:
    print(f"O número {entrada} pertence à sequência de Fibonacci.")
else:
    print(f"O número {entrada} não pertence à sequência de Fibonacci.")