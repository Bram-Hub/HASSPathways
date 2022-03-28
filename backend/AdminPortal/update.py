import boto3
import json
import os
import decimal
from datetime import datetime

session = boto3.Session(region_name='us-east-1', profile_name='auto')
db = session.resource('dynamodb')

tab = db.Table('course_database').scan()

for i in tab['Items']:
    for j in i:
        if(type(i[j]) == decimal.Decimal):
            i[j] = int(i[j])

courses = []
for x in range(len(tab['Items'])):
    outerFields = dict()
    outerFields["info"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    outerFields["pk"] = tab['Items'][x]['pk']
    outerFields["model"] = "database.course"
    innerFields = dict()
    innerFields["prefix"] = tab['Items'][x]['prefix']
    innerFields["ID"] = tab['Items'][x]['ID'] 
    innerFields["name"] = tab['Items'][x]['name']
    innerFields["description"] = tab['Items'][x]['description']
    innerFields["HI"] = tab['Items'][x]['HI']
    innerFields["CI"] = tab['Items'][x]['CI']
    innerFields["DI"] = tab['Items'][x]['DI']
    innerFields["major_restrictive"] = tab['Items'][x]['major_restrictive']
    innerFields["fall"] = tab['Items'][x]['fall']
    innerFields["spring"] = tab['Items'][x]['spring']
    innerFields["summer"] = tab['Items'][x]['summer']
    outerFields["fields"] = innerFields
    courses.append(outerFields)

print(courses)
courseDataFile = open("courses.json", 'w')
courseDataFile.truncate()
courseDataFile.write(json.dumps(courses, sort_keys=True, indent=4))
courseDataFile.close()
