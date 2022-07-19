# This scraper is mainly sourced from the QUACs team and
# is a modified version of their catalog scraper

from typing import Dict, List, Tuple
import requests
import sys
from lxml import html
import os
from tqdm import tqdm
import json
from lxml import etree
import csv

# The api key is public so it does not need to be hidden in a .env file
BASE_URL = "http://rpi.apis.acalog.com/v1/"
# It is ok to publish this key because I found it online already public
DEFAULT_QUERY_PARAMS = "?key=3eef8a28f26fb2bcc514e6f1938929a1f9317628&format=xml"
CHUNK_SIZE = 500

# returns the list of catalogs with the newest one being first
# each catalog is a tuple (year, catalog_id) ex: ('2020-2021', 21)
def get_catalogs() -> List[Tuple[str, int]]:
    catalogs_xml = html.fromstring(
        requests.get(
            f"{BASE_URL}content{DEFAULT_QUERY_PARAMS}&method=getCatalogs"
        ).text.encode("utf8")
    )
    catalogs = catalogs_xml.xpath("//catalogs/catalog")

    ret: List[Tuple[str, int]] = []
    # For each catalog get its year and id and add that as as tuples to ret
    for catalog in catalogs:
        catalog_id: int = catalog.xpath("@id")[0].split("acalog-catalog-")[1]
        catalog_year: str = catalog.xpath(".//title/text()")[0].split(
            "Rensselaer Catalog "
        )[1]
        ret.append((catalog_year, catalog_id))

    # sort so that the newest catalog is always first
    ret.sort(key=lambda tup: tup[0], reverse=True)
    return ret


# Returns a list of course ids for a given catalog
def get_course_ids(catalog_id: str) -> List[str]:
    courses_xml = html.fromstring(
        requests.get(
            f"{BASE_URL}search/courses{DEFAULT_QUERY_PARAMS}&method=listing&options[limit]=0&catalog={catalog_id}"
        ).text.encode("utf8")
    )
    return courses_xml.xpath("//id/text()")


# Finds and returns a cleaned up description of the course
def get_catalog_description(fields, course_name):
    found_name = False
    # The description is always the next full field after the course name field
    # Itearte through the fields until we find the course name field and then return the next filled field
    for field in fields:
        if found_name == False:
            name = field.xpath(".//*/text()")
            if name and name[0] == course_name:
                found_name = True
        else:
            description = field.xpath(".//*/text()")
            if description:
                clean_description = " ".join(" ".join(description).split())
                # Short descriptions are usually false positives
                if clean_description.startswith("Prerequisite"):
                    return ""
                elif len(clean_description) > 10:
                    return clean_description

    return ""

def obtain_CI(name):
    csv_file = open('CI_classes.csv', 'r')
    reader = csv.reader(csv_file)

    for row in reader:
        course_name = row[3]
        if name.strip().lower() == course_name.strip().lower():
            return True

    return False

def get_course_data(course_ids: List[str]) -> Dict:
    data = {}
    # Break the courses into chunks of CHUNK_SIZE to make the api happy
    course_chunks = [
        course_ids[i : i + CHUNK_SIZE] for i in range(0, len(course_ids), CHUNK_SIZE)
    ]

    depts = []

    f = open('depts.json', 'r')
    f = json.load(f)

    for dept in f:
        depts.append(dept)

    for chunk in course_chunks:
        ids = "".join([f"&ids[]={id}" for id in chunk])
        url = f"{BASE_URL}content{DEFAULT_QUERY_PARAMS}&method=getItems&options[full]=1&catalog={catalog_id}&type=courses{ids}"

        courses_xml = html.fromstring(requests.get(url).text.encode("utf8"))
        courses = courses_xml.xpath("//courses/course[not(@child-of)]")
        for course in courses:
            subj = course.xpath("./content/prefix/text()")[0].strip()
            if not (subj in depts):
                continue
            ID = course.xpath("./content/code/text()")[0].strip()
            if ID[0] == '6':
                continue
            course_name = course.xpath("./content/name/text()")[0].strip()
            fields = course.xpath("./content/field")
            fall = False
            spring = False
            summer = False
            even = False
            odd = False
            offered_text = ""
            prereqs = "None"

            for field in fields:
                if field.get("type") == 'acalog-field-519':
                    field_text = field.xpath("./data/text()")
                    if len(field_text) > 0:
                        # print(field_text)
                        field_text = field_text[0].strip().lower()
                        if "fall" in field_text:
                            fall = True
                        if "spring" in field_text:
                            spring = True
                        if "summer" in field_text:
                            summer = True
                        if "even" in field_text:
                            even = True
                        if "odd" in field_text:
                            odd = True
                        offered_text = field_text
                elif field.get("type") == 'acalog-field-517':
                    field_text = field.xpath("./data/p/text()")
                    if len(field_text) > 0:
                        prereqs = field_text[0].strip()

            data[course_name] = {
                "subj": subj,
                "ID": ID,
                "name": course_name,
                "description": get_catalog_description(fields, course_name),
                "offered": {
                    "fall": fall,
                    "spring": spring,
                    "summer": summer,
                    "odd": odd,
                    "even": even,
                    "text": offered_text
                },
                "properties": {
                    "CI": obtain_CI(course_name),
                    "HI": True if subj == "IHSS" else False,
                    "major_restricted": False
                },
                "prerequisites": prereqs
            }

    return data

if __name__ == "__main__":
    if sys.argv[-1] == "help" or sys.argv[-1] == "--help":
        print(f"USAGE: python3 {sys.argv[0]} [ALL_YEARS]")
        sys.exit(1)

    catalogs = get_catalogs()

    if sys.argv[-1] != "ALL_YEARS":
        print("Parsing single year")
        catalogs = catalogs[:1]
    else:
        print("Parsing all years")

    for index, (year, catalog_id) in enumerate(tqdm(catalogs)):
        course_ids = get_course_ids(catalog_id)
        data = get_course_data(course_ids)

        f = open('courses.json', 'w')
        json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
        f.close()
