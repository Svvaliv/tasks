# Есть файл meetings.csv, в котором хранятся имена, фамилии людей, а так же дата и время встречи
# с этими людьми. Нужно вывести имена и фамилии людей в порядке возрастания дат

import csv
import heapq
from collections import namedtuple
from datetime import datetime

with open('data/meetings.csv') as fi:
    meetings = csv.DictReader(fi)
    Friend = namedtuple('Friend', meetings.fieldnames)
    sort_meetings = []
    for meeting in meetings:
        friend = Friend(**meeting)
        dt = datetime.strptime(friend.meeting_date + friend.meeting_time, '%d.%m.%Y%H:%M')
        heapq.heappush(sort_meetings, (dt, friend))

length = len(sort_meetings)
for _ in range(length):
    _, meeting = heapq.heappop(sort_meetings)
    print(f'{meeting.surname} {meeting.name}')
