def data_out(name, surname, date_birth, city, email, phone_number):
    print(name, surname, date_birth, city, email, phone_number, sep=', ')


if __name__ == '__main__':
    data = {}
    config = ['name', 'surname', 'date_birth', 'city', 'email', 'phone_number']
    for i in config:
        data[i] = input(f'Введите значение поля {i}: ')

    data_out(surname=data['surname'], name=data['name'], date_birth=data['date_birth'], city=data['city'], email=data['email'], phone_number=data['phone_number'])
