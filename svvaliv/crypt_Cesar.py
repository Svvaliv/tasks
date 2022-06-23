ru_upper_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТЦФХЦЧШЩЪЫЬЭЮЯ'
ru_lower_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
en_upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_lower_letters = 'abcdefghijklmnopqrstuvwxyz'

crypt = input('Что нужно сделать? Зашифровать - crypt, дешифровать - decrypt: ')
lang = input('Какой язык используем? Английский - en, русский - ru: ')
k = int(input('Шаг сдвига: '))

#Блажен, кто верует, тепло ему на свете!
def decrypt_ru(string, key):
    r = ''
    for c in string:
        if c.isalpha():
            if c.isupper():
                r += ru_upper_letters[ru_upper_letters.find(c) - key]
            else:
                r += ru_lower_letters[ru_lower_letters.find(c) - key]
        else:
            r += c
    return r

def decrypt_en(string, key):
    r = ''
    for c in string:
        if c.isalpha():
            if c.isupper():
                r += en_upper_letters[en_upper_letters.find(c) - key]
            else:
                r += en_lower_letters[en_lower_letters.find(c) - key]
        else:
            r += c
    return r

def crypt_ru(string, key):
    r = ''
    len_up = len(ru_upper_letters)
    len_low = len(ru_lower_letters)
    for c in string:
        if c.isalpha():
            if c.isupper():
                r += ru_upper_letters[-(len_up - ru_upper_letters.find(c) - key)]
            else:
                r += ru_lower_letters[-(len_low - ru_lower_letters.find(c) - key)]
        else:
            r += c
    return r

def crypt_en(string, key):
    r = ''
    len_up = len(en_upper_letters)
    len_low = len(en_lower_letters)
    for c in string:
        if c.isalpha():
            if c.isupper():
                r += en_upper_letters[-(len_up - en_upper_letters.find(c) - key)]
            else:
                r += en_lower_letters[-(len_low - en_lower_letters.find(c) - key)]
        else:
            r += c
    return r



if crypt == 'crypt':
    string = input('Введите текст для шифровки: ')
    if lang == 'ru':
        print(crypt_ru(string, k))
    elif lang == 'en':
        print(crypt_en(string, k))

if crypt == 'decrypt':
    string = input('Введите текст для дешифровки: ')
    if lang == 'ru':
        print(decrypt_ru(string, k))
    elif lang == 'en':
        print(decrypt_en(string, k))