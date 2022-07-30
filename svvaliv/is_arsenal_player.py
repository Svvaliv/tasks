'''
Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов, каждый из
которых содержит информацию о каком-либо футболисте:

{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}
У футболиста имеются следующие атрибуты:

first_name — имя
last_name — фамилия
team — название футбольного клуба
position — игровая позиция

Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих
за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении —
в лексикографическом порядке фамилий, каждый на отдельной строке.

При этом не гарантируется, что json файл будет валидным
'''

import json
from zipfile import ZipFile


# Функция для проверки json на валидность
def is_correct_json(string: bytes) -> (bool, json):
    try:
        return json.loads(string)
    except (json.decoder.JSONDecodeError, UnicodeDecodeError):
        return False


# Создаём список игроков из Арсенала. Пробегаемся по всем файлам из архива, проверяем каждый на валидность,
# и если файл валиден и игрок играет в Арсенале, то добавляем его в список
players = []
with ZipFile('data/data.zip') as zf:
    for file in zf.namelist():
        with zf.open(file) as fi:
            player = is_correct_json(fi.read())
            if player and player['team'] == 'Arsenal':
                players.append(f'{player["first_name"]} {player["last_name"]}')

# Выводи имена игроков в лексикографическом порядке
for name in sorted(players):
    print(name)
