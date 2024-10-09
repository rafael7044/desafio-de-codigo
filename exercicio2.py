def is_fibonacci(num):
    a, b = 0, 1

    # Se o número for 0 ou 1, ele já pertence à sequência
    if num == 0 or num == 1:
        return True


    while b <= num:
        if b == num:
            return True
        a, b = b, a + b

    return False  # Se a sequência passa do número, ele não pertence


numero = int(input("Informe um número: "))


if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

