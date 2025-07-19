def factorial(number):
    if number < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def valid_int_number():

    while True:
        number = input('digit um número inteiro: ')
        try:
            number = int(number)

            if number < 0:
                print('Erro: O número não pode ser negativo.')
                continue

            return number

        except ValueError:
            print('Por Favor entre com um numero inteiro e positivo!')


if __name__ == '__main__':

    number = valid_int_number()
    print(f'fatorial de {number} é: {factorial(number)}')