def int_func(text):
    return ''.join([text[i].upper() if i == 0 else text[i] for i in range(len(text))])


def all_func(text):
    return ' '.join([int_func(i) for i in text])



if __name__ == '__main__':
    word = input('Введите строку: ').split()
    print(all_func(word))
