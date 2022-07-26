import csv
import json
from datetime import datetime

with open('data/exam_results.csv', encoding='utf-8') as fi, \
        open('data/best_scores.json', 'w', encoding='utf-8') as fo:
    students = csv.DictReader(fi)
    students_out = {}
    for student in students:
        student_info = {
            'name': student['name'],
            'surname': student['surname'],
            'best_score': int(student['score']),
            'date_and_time': student['date_and_time'],
            'email': student['email']
        }
        key = student['name'] + ' ' + student['surname']
        if key in students_out:
            now_date = datetime.fromisoformat(student['date_and_time'])
            exam_date = datetime.fromisoformat(students_out[key]['date_and_time'])
            now_score, exam_score = int(student['score']), int(students_out[key]['best_score'])
            if now_score > exam_score:
                students_out[key]['best_score'] = int(student['score'])
                students_out[key]['date_and_time'] = student['date_and_time']
            elif now_score == exam_score and now_date > exam_date:
                students_out[key]['date_and_time'] = student['date_and_time']
        else:
            students_out[key] = student_info
    students_out = [info for info in sorted(students_out.values(), key=lambda item: item['email'])]
    json.dump(students_out, fo, indent=3)
