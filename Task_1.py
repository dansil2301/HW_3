def division(number_1: float, number_2: float):
    try:
        div = number_1 / number_2
    except:
        print('Ошибка! Деление на 0')
        div = None
    return div

if __name__ == '__main__':
    number_1 = float(input('Введите первое число: '))
    number_2 = float(input('Введите второе число: '))
    print(division(number_1, number_2))