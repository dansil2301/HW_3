def my_func(x, y):
    x_times = x
    for i in range(-1 * y - 1):
        x *= x_times

    return 1 / x


if __name__ == '__main__':
    vozvod = int(input('Введите число, которое нужно возвести в степень: '))
    stepen = int(input('Введите степень: '))
    print(my_func(vozvod, stepen))