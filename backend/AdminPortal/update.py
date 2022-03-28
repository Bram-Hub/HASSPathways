import boto3
import json
import os
import decimal
from datetime import datetime

session = boto3.Session(region_name='us-east-1', profile_name='auto')
db = session.resource('dynamodb')

course_data = db.Table('courses').scan()
pathway_data = db.Table('pathways').scan()

for i in pathway_data['Items']:
    for j in i:
        if(type(i[j]) == decimal.Decimal):
            i[j] = int(i[j])
        elif(type(i[j]) == list):
            for k in range(len(i[j])):
                i[j][k] = int(i[j][k])

for i in course_data['Items']:
    for j in i:
        if(type(i[j]) == decimal.Decimal):
            i[j] = int(i[j])

print(pathway_data['Items'])

courses = []
for x in range(len(course_data['Items'])):
    outerFields = dict()
    outerFields["info"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    outerFields["pk"] = course_data['Items'][x]['pk']
    outerFields["model"] = "database.course"
    innerFields = dict()
    innerFields["prefix"] = course_data['Items'][x]['prefix']
    innerFields["ID"] = course_data['Items'][x]['ID'] 
    innerFields["name"] = course_data['Items'][x]['name']
    innerFields["description"] = course_data['Items'][x]['description']
    innerFields["HI"] = course_data['Items'][x]['HI']
    innerFields["CI"] = course_data['Items'][x]['CI']
    innerFields["DI"] = course_data['Items'][x]['DI']
    innerFields["major_restrictive"] = course_data['Items'][x]['major_restrictive']
    innerFields["fall"] = course_data['Items'][x]['fall']
    innerFields["spring"] = course_data['Items'][x]['spring']
    innerFields["summer"] = course_data['Items'][x]['summer']
    outerFields["fields"] = innerFields
    courses.append(outerFields)

pathways = []
for x in range(len(pathway_data['Items'])):
    outerFields = dict()
    outerFields["info'"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    outerFields["pk"] = pathway_data['Items'][x]['pk']
    outerFields["model"] = "database.pathway"

    innerFields = dict()
    innerFields["pathName"] = pathway_data['Items'][x]['pathName']
    innerFields["pathDescript"] = pathway_data['Items'][x]['pathDescript']
    innerFields["priority1"] = pathway_data['Items'][x]['priority1'].copy()
    innerFields["priority2"] = pathway_data['Items'][x]['priority2'].copy()
    innerFields["priority3"] = pathway_data['Items'][x]['priority3'].copy()

    outerFields["fields"] = innerFields
    pathways.append(outerFields)



print(courses)
courseDataFile = open("courses.json", 'w')
pathwayDataFile = open("pathways.json", "w")
courseDataFile.truncate()
pathwayDataFile.truncate()
courseDataFile.write(json.dumps(courses, sort_keys=True, indent=4))
pathwayDataFile.write(json.dumps(pathways, sort_keys=True, indent=4))
courseDataFile.close()
pathwayDataFile.close()
