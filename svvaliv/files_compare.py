'''
Доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения,
разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...
Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы, и
выводит полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены в
лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.

Примечание 1. Например, если бы файл files.txt имел вид:

input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB
то программа должна была бы вывести:

boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB
где Summary — общий объем файлов группы.

Примечание 2. Гарантируется, что все имена файлов содержат расширение.

Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально возможных) единицах измерения с
округлением до целых. Другими словами, сначала следует определить суммарный объем всех файлов группы, скажем,
в байтах, а затем перевести полученное значение в самые крупные (максимально возможные) единицы измерения.
Примеры перевода:

1023 B -> 1023 B
1300 B -> 1 KB
1900 B -> 2 KB
Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
'''


# Функция преобразует байты
def convert_bytes(num: int) -> str:
    step_unit = 1024
    for unit in ['B', 'KB', 'MB', 'GB']:
        if num < step_unit:
            return f'{round(num)} {unit}'
        num /= step_unit


expansions = {}
units = {
    'B': 1,
    'KB': 1024,
    'MB': 1024 ** 2,
    'GB': 1024 ** 3,
}

# Получаем список строк из файла
with open('data/files.txt', encoding='utf-8') as f:
    files = [file.strip() for file in f.readlines()]

# Создаём словарь, в котором ключами являются расширения файлов, а значениями - список кортежей
# с названием файла и его размером, предварительно преобразуя размер в байты
for file in files:
    filename, filesize, fileunit = file.split()
    index = filename.rfind('.')
    key = filename[index:]
    bytes_size = int(filesize) * units[fileunit]
    expansions.setdefault(key, []).append((filename, bytes_size))

# Выводим результат на печать. Берем по очереди расширения (expansion), отсортированные в лексикографическом порядке,
# затем имя файла и его размер по ключу expansion, отсортированные по имени файла, в конце преобразуем размер файла
# из байтов по условию задачи, и выводим всё это на печать
for expansion in sorted(expansions):
    size = 0
    for filename, filesize in sorted(expansions[expansion]):
        print(filename)
        size += filesize
    print('-' * 10)
    print(f'Summary: {convert_bytes(size)}\n')
