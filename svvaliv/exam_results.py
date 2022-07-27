# Есть файл exam_results.csv, в котором записаны данные о результатах экзаменов студентов.
# Некоторые студенты записаны несколько раз, т.к. ходили на пересдачи.
# В файле хранится имя, фамилия студента, оценка, дата экзамена или пересдачи и email
# Нужно для всех студентов найти их лучшую оценку и записать информацию в файл best_sores.json
# Если оценка на пересдаче совпадает с полученной ранее, то в результате нужно записать дату пересдачи
# Информацию нужно сохранять в лексикографическом порядке email

import csv
import json
from datetime import datetime

with open('data/exam_results.csv', encoding='utf-8') as fi, \
        open('data/best_scores.json', 'w', encoding='utf-8') as fo:
    students = csv.DictReader(fi)
    students_out = {}
    for student in students:
        # Формируем информацию о студенте
        student_info = {
            'name': student['name'],
            'surname': student['surname'],
            'best_score': int(student['score']),
            'date_and_time': student['date_and_time'],
            'email': student['email']
        }
        key = student['email']
        # Проверяем, есть ли уже информация о студенте в исходящем словаре
        if key in students_out:
            now_date = datetime.fromisoformat(student['date_and_time'])
            exam_date = datetime.fromisoformat(students_out[key]['date_and_time'])
            now_score, exam_score = int(student['score']), int(students_out[key]['best_score'])
            # Если оценка на пересдаче выше, чем на экзамене или другой пересдаче, то
            # перезаписываем соответствующую информацию (оценку и дату)
            if now_score > exam_score:
                students_out[key]['best_score'] = int(student['score'])
                students_out[key]['date_and_time'] = student['date_and_time']
            # Если же оценка равна той, что получена ранее, то меняем только дату
            elif now_score == exam_score and now_date > exam_date:
                students_out[key]['date_and_time'] = student['date_and_time']
        # Если же информации о студенте еще нет, то добавляем её в словарь
        else:
            students_out[key] = student_info
    # Сортируем словарь по email в лексикографическом порядке и сохраняем результат в файл
    students_out = [students_out[key] for key in sorted(students_out)]
    json.dump(students_out, fo, indent=3)
