'''
Добавляете этот код к своей программе (если в уроке есть архив с тестовыми данными).
Переменной "filename" присваиваете значение - путь до файла с тестовыми данными.
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
    '''Функция распаковывет архив с тестовыми данными, затем выполняет код из каждого файла и выводит
    результат выполнения вашего кода и ожидаемый результат'''
    from zipfile import ZipFile

    with ZipFile(filename) as z:
        length = len(z.namelist()) // 2
        files = [(code, out) for code, out in zip(z.namelist()[::2], z.namelist()[1::2])]
        for file_exec, file_out in files:
            with z.open(name=file_exec) as fi:
                with z.open(name=file_out) as fo:
                    code, out = fi.read().decode(), fo.read().decode()
                    print(f'Тест № {file_exec} из {length}')
                    print(f'\nКод: \n\n{code}\n')
                    print('-' * 100)
                    print('Ваш результат:')
                    try:
                        exec(code)
                        print(f"{'-' * 100}\nОжидаемый результат:\n{out}\n{'*' * 100}")
                    except Exception as e:
                        print(f'{"🚫" * 50}\n"Тест № {file_exec} завершился с `ошибкой "{type(e).__name__}: {e}\n')
                        print(f'Ожидаемый результат: \n{out}\n{"🚫" * 50}"\n')


filename = 'data/tests/tests_2777710.zip'
testing_lesson(filename)
