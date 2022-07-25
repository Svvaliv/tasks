# Есть 4 csv файла (quarter_n.csv), в котором указан товар и количество проданных единиц этого товара
# за определенный квартал года
# Так же доступен файл prices.json, в котором указана цена за каждый товар
# Необходимо посчитать общую заработанную сумму за год

import csv
import json
from collections import Counter


def sales_counter(filename: str) -> Counter:
    with open(filename, encoding='utf-8') as fi:
        _, *products = csv.reader(fi)
        count = Counter()
        for product in products:
            name, total_count = product[0], sum(map(int, product[1:]))
            count.update({name: total_count})
    return count


with open('data/prices.json', encoding='utf-8') as js:
    prices = json.load(js)

counter = Counter()
files = ['data/quarter1.csv', 'data/quarter2.csv', 'data/quarter3.csv', 'data/quarter4.csv']
for file in files:
    counter.update(sales_counter(file))

total_earned = 0
for product in counter:
    total_earned += prices[product] * counter[product]

print(f'За год заработано {total_earned} руб.')
