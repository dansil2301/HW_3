def new_sum(s, ls_num):
    return s + sum(ls_num)


if __name__ == '__main__':
    s = 0
    numbers = []
    while True:
        numbers = input('Введите число: ').split()

        if numbers[0] == '!с':
            break

        numbers = list(map(int, numbers))

        s = new_sum(s, numbers)
        print(s)