#!/usr/bin/env python3

# run directly with python sis_scraper.py
 
import aiohttp
import asyncio
import json
import courses_scraper
from datetime import date
from bs4 import BeautifulSoup
import pandas as pd
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


async def main():
    term = get_closest_semester()
    subjects = get_departments()

    ci_courses = await get_all_ci_courses(term, subjects)


    df = []
    for course in ci_courses:
        df.append([course[:4], course[5:9], course[12:]])
    df = pd.DataFrame(df, columns = ["SUBJECT", "ID", "NAME"])
    df.to_csv("ci_courses.csv", index = False)




if __name__ == '__main__':
    asyncio.run(main())
