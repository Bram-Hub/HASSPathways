import json
import aiohttp
import re
import asyncio
from bs4 import BeautifulSoup
from tqdm import tqdm

async def get_details(course, year):
    if course[0] == None or course[1] == None:
        return None

    fall = str(year[0:4]) + '09'
    spring = str(year[-4:]) + '01'
    summer = str(year[-4:]) + '05'
    full_soup = None

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=5)) as session:
        async with session.post(
                "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse",
                data = f"term_in={fall}&subj_in={course[1][:4]}&crse_in={course[1][-4:]}&schd_in=L"
        ) as request:
            html = await request.text()

        soup = BeautifulSoup(html, 'html.parser')
        if soup.find(text=re.compile("No classes were found")) == None:
            fall = True
            full_soup = soup
        else:
            fall = False

        async with session.post(
                "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse",
                data = f"term_in={spring}&subj_in={course[1][:4]}&crse_in={course[1][-4:]}&schd_in=L"
        ) as request:
            html = await request.text()

        soup = BeautifulSoup(html, 'html.parser')
        if soup.find(text=re.compile("No classes were found")) == None:
            spring = True
            full_soup = soup
        else:
            spring = False

        async with session.post(
                "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse",
                data = f"term_in={summer}&subj_in={course[1][:4]}&crse_in={course[1][-4:]}&schd_in=L"
        ) as request:
            html = await request.text()

        soup = BeautifulSoup(html, 'html.parser')
        if soup.find(text=re.compile("No classes were found")) == None:
            summer = True
            full_soup = soup
        else:
            summer = False

        if full_soup == None:
            return None

        rows = full_soup.find_all('table', class_="datadisplaytable")[0].find_all('tr')
        if len(rows) >= 2:
            title = rows[0].get_text()
            attr = rows[1].get_text()
            if course[0].upper() in title.upper():
                return {
                    "ID": course[1][-4:],
                    "cross listed": [],
                    "description": "No description available, course not listed on catalog, prereqs/crosslisted not checked.",
                    "name": course[0],
                    "offered": {
                      "even": False,
                      "fall": fall,
                      "odd": False,
                      "spring": spring,
                      "summer": summer,
                      "text": ""
                    },
                    "prerequisites": [],
                    "professors": [],
                    "properties": {
                      "CI": True if "Communication Intensive" in attr else False,
                      "HI": True if "HASS Inquiry" in attr else False,
                      "major_restricted": False
                    },
                    "subj": course[1][:4]
                }
    return None

async def fill(folder_path):
    f1 = open(folder_path + '/pathways.json', 'r')
    f2 = open(folder_path + '/courses.json', 'r')

    pathways = json.load(f1)
    courses = json.load(f2)
    f1.close()
    f2.close()

    for pathway in tqdm(pathways):
        p_courses = []
        for typ in pathways[pathway]:
            if typ != 'minor' and typ != 'name' and \
            typ != 'description' and typ != 'remaining_header':
                for p_course in pathways[pathway][typ]:
                    p_courses.append([p_course, pathways[pathway][typ][p_course]])

        for course in p_courses:
            if not course[0] in courses:
                tmp = await get_details(course, folder_path[-9:])
                if tmp != None:
                    courses[course[0]] = tmp

    f2 = open(folder_path + '/courses.json', 'w')
    json.dump(courses, f2, sort_keys=True, indent=2, ensure_ascii=False)
    f2.close()