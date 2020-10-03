import os, csv
from main.models import (
    Ivent,
    Organizer
)

with open('orgs.csv', 'r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        p=Organizer(name=row['name'], description=row['description'], link=row['link'])
        p.save()

with open('ivents.csv', 'r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        p=Ivent(title=row['title'], description=row['description'], organizer_id=row['organizer_id'], area=row['area'])
        p.save()

