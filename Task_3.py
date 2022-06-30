def my_func(f_el, s_el, t_el):
    s = 0
    if f_el <= s_el and f_el <= t_el:
        s = s_el + t_el
    elif s_el <= f_el and s_el <= t_el:
        s = f_el + t_el
    else:
        s = f_el + s_el
    return s


if __name__ == '__main__':
    numbers = []
    for i in range(3):
        numbers.append(int(input(f'Введите {i + 1} число: ')))
    print(my_func(numbers[0], numbers[1], numbers[2]))