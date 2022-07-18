#!/usr/bin/env python3

# run directly with python sis_scraper.py
 
import aiohttp
import asyncio
import json
import courses_scraper
from datetime import date
from bs4 import BeautifulSoup
# import pandas as pd
# Scrapes sis.rpi.edu to get Communication Intensive attributes and rewrites
# courses.json to update the information.
#
# We can query for a bunch of different terms. I am going to simply grab the
# nearest term.
# 
# An example term is 202209 which is f"{YEAR}{MONTH}" where the possible months
# are 1, 5, 9, 12. For more details on available semesters see the following
# code from quacs sis scraper:
# 
# https://github.com/quacs/quacs/blob/master/scrapers/sis_scraper/util.py#L42-L85


def get_ci_courses(text):
    soup = BeautifulSoup(text, 'html.parser')
    table = soup.find('table', {"class": "datadisplaytable"})
    table_text = str(table)
    entries = table_text.split("<tr>")[1:]
    titles = entries[::2]
    details = entries[1::2]

    ci_courses = []
    for i in range(len(titles)):
        title = BeautifulSoup(titles[i], features='lxml').find('a').get_text()
        course_details = details[i]
        if "Course Attributes: " in course_details \
        and "Communication Intensive" in course_details:
            ci_courses.append(title)

    return ci_courses

def get_departments():
    f = open("depts.json")
    data = json.load(f)
    f.close()
    return data
 
def get_closest_semester():
    d = date.today()
    month = d.month
    year = d.year
    RPI_MONTHS = {1, 5, 9, 12}
    while month not in RPI_MONTHS:
        month -= 1
        if month == 0: month = 12; year -= 1;

    # append a 0 to the month if need be
    month = str(month)
    month = "0" + month if len(month) == 1 else month
    return f"{year}{month}"

async def get_all_ci_courses(term, subjects):
    ci_courses = []
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=5)) as session:
        # Query all subjects
        for subj in subjects:
            async with session.post(
                "https://sis.rpi.edu/rss/bwckctlg.p_display_courses",
                data=f"term_in={term}&call_proc_in=&sel_subj=dummy&sel_levl=dummy&sel_schd=dummy&sel_coll=dummy&sel_divs=dummy&sel_dept=dummy&sel_attr=dummy&sel_subj={subj}&sel_crse_strt=&sel_crse_end=&sel_title=&sel_levl=%25&sel_schd=%25&sel_coll=%25&sel_divs=%25&sel_dept=%25&sel_from_cred=&sel_to_cred=&sel_attr=%25",
            ) as request:
                html = await request.text()
                print(f"Finished getting {subj}")
                ci_courses += get_ci_courses(html)
    return ci_courses


async def scrape_ci_sis(year = None, semester_type = None):
    term = ""
    if year is not None and semester_type is None:   raise Exception("invalid input arguments")
    elif year is None and semester_type is not None: raise Exception("invalid input arguments")
    elif year is None and semester_type is None:
        term = get_closest_semester()
    elif year is not None and semester_type is not None:
        possible_semesters = {"spring": "01", "summer": "05", "fall": "09", "winter": "12"}

        if semester_type not in possible_semesters: raise Exception(f"Invalid semester inputted for SIS scraper. Possible values: {possible_semesters.keys()}.")
        if len(str(year)) != 4: raise Exception("Invalid year inputted into SIS scraper. Use a value such as 20XX.")

        sem_num = possible_semesters[semester_type]
        term = str(year) + sem_num

    subjects = get_departments()

    ci_courses = await get_all_ci_courses(term, subjects)

    overwrite_courses_json(ci_courses)


    # Uncomment below if a csv file for CI classes needs to be created
    # df = []
    # for course in ci_courses:
    #     df.append([course[:4], course[5:9], course[12:]])
    # df = pd.DataFrame(df, columns = ["SUBJECT", "ID", "NAME"])
    # df.to_csv("ci_courses.csv", index = False)

def overwrite_courses_json(ci_courses):
    json_path = "../../frontend/src/data/json/courses.json"
    set_ci_courses = set()
    for i in ci_courses:
        ci_id = f"{i[:4]} {i[5:9]}"
        set_ci_courses.add(ci_id)

    f = open(json_path)
    courses= json.load(f)
    f.close()
    for i in courses.keys():
        value = courses[i]
        courses_id = f"{value['subj']} {value['ID']}"
        if courses_id in set_ci_courses:
            courses[i]["properties"]["CI"] = True
    with open(json_path, "w") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    asyncio.run(scrape_ci_sis())
