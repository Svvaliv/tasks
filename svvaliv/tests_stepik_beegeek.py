'''
Добавляете этот код к своей программе (если в уроке есть архив с тестовыми данными).
Переменной "filename" присваиваете значение - путь до файла с тестовыми данными
Запускаете программу. Если всё правильно, вывод будет примерно таким:
Ваш результат:
1
-2
----------------------------------------------------------------------------------------------------
Ожидаемый результат:
1
-2
****************************************************************************************************
...
'''

def testing_lesson(filename: str):
    from zipfile import ZipFile

    with ZipFile(filename) as z:
        p = filename[:-4]
        z.extractall(path=p)
        length = len(z.namelist())

    for i in range(1, length // 2 + 1):
        with open(f'{p}/{i}') as fi:
            with open(f'{p}/{i}.clue') as fo:
                print('Ваш результат:')
                exec(fi.read())
                print('-' * 100)
                print('Ожидаемый результат:')
                print(fo.read())
                print('*' * 100)


filename = 'data/tests/tests_2777710.zip'
testing_lesson(filename)
