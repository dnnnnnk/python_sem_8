from return_data_file import data_file

def copy_data():
    data, nf = data_file()
    count_rows = len(data)
    number_row = int(input(f"Введите номер копируемой строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер копируемой строки "
                               f"от 1 до {count_rows}: "))
    target = int(input('В какой файл скопировать? '))
    while target < 1 or target > 2:
        target = int(input("Ошибка! Укажите номер файла от 1 до 2: "))

    copy = data[number_row-1]

    with open(f'db/data_{target}.txt', 'a', encoding='utf-8') as file:
        file.write('\n' + copy)