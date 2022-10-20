import boto3
import json
import os
from datetime import datetime

session = boto3.Session(region_name='us-east-1', profile_name='auto')
db = session.resource('dynamodb')

courseTab = db.Table("courses")
pathwayTab = db.Table("pathways")

def dataCourses(id, CI, DI, HI, ID, descr, f, mr, nm, pre, sp, sm, pk):
	response = courseTab.put_item(
		Item={
			 'id': str(id),
			 'CI': CI,
			 'DI': DI,
			 'HI': HI,
			 'ID': ID,
			 'description': descr,
			 'fall': f,
			 'major_restrictive': mr,
			 'name': nm,
			 'prefix': pre,
			 'spring': sp,
			 'summer': sm,
			 'pk': pk
		}
	)

	return response

def dataPathways(id, pd, pn, p1, p2, p3, pk):
	response = pathwayTab.put_item(
		Item={
			 'id': str(id),
			 'pathDescript': pd,
			 'pathName': pn,
			 'priority1': p1,
			 'priority2': p2,
			 'priority3': p3,
			 'pk': pk
		}
	)

	return response
	

if __name__ == "__main__":
	file = open('courses.json', 'r')
	courseData = json.load(file)
	filep = open('pathways.json', 'r')
	pathwayData = json.load(filep)

	k=0
	for i in courseData:
		print(dataCourses(k, i['fields']['CI'], i['fields']['DI'], i['fields']['HI'], i['fields']['ID'],
			i['fields']['description'], i['fields']['fall'], i['fields']['major_restrictive'],
			i['fields']['name'], i['fields']['prefix'], i['fields']['spring'], i['fields']['summer'],
			i['pk']))
		k+=1

	i = 0
	for j in pathwayData:
		print(dataPathways(i, j['fields']['pathDescript'], j['fields']['pathName'], j['fields']['priority1'],
			j['fields']['priority2'], j['fields']['priority3'], j['pk']))

		i+=1




