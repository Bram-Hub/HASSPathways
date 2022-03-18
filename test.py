import boto3
import json
import os
import decimal
from datetime import datetime

table = boto3.client(
    'dynamodb',
    aws_access_key_id = 'AKIAQCXQDGTMK5635ZYL',
    aws_secret_access_key = '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',
    region_name = 'us-east-1'
    )

db = boto3.resource(
    'dynamodb',
    aws_access_key_id = 'AKIAQCXQDGTMK5635ZYL',
    aws_secret_access_key = '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',
    region_name = 'us-east-1'
    )

tab = db.Table('course_database').scan()

print(tab['Items'][0]['fall'])

for i in tab['Items']:
    for j in i:
        if(type(i[j]) == decimal.Decimal):
            i[j] = int(i[j])
    print(i)

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