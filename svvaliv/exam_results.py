import csv
import json

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
            if int(student['score']) >= int(students_out[key]['best_score']):
                students_out[key]['best_score'] = int(student['score'])
                students_out[key]['date_and_time'] = student['date_and_time']
        else:
            students_out[key] = student_info
    students_out = [info for info in sorted(students_out.values(), key=lambda item: item['email'].lower())]
    json.dump(students_out, fo, indent=3)
