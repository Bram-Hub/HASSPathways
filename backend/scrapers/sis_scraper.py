import json
import aiohttp
import re
import asyncio
from bs4 import BeautifulSoup
from tqdm import tqdm


import json
import aiohttp
import re
import asyncio
from bs4 import BeautifulSoup
from tqdm import tqdm

async def get_details(ID, subj, curr_year, session):
    years = []
    for i in range(-2, 1):
        new_year = str(int(curr_year[0:4])+i) + str(int(curr_year[-4:])+i)
        years.append(new_year)

    dets = [False, set()]

    for year in years:
        fall = str(year[0:4]) + '09'
        spring = str(year[-4:]) + '01'
        summer = str(year[-4:]) + '05'
        full_soup = None

        async with session.post(
                "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse",
                data = f"term_in={fall}&subj_in={subj}&crse_in={ID}&schd_in=L"
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
                data = f"term_in={spring}&subj_in={subj}&crse_in={ID}&schd_in=L"
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
                data = f"term_in={summer}&subj_in={subj}&crse_in={ID}&schd_in=L"
        ) as request:
            html = await request.text()

        soup = BeautifulSoup(html, 'html.parser')
        if soup.find(text=re.compile("No classes were found")) == None:
            summer = True
            full_soup = soup
        else:
            summer = False

        if full_soup == None:
            return dets

        times = full_soup.findAll("table", {
            "class": "datadisplaytable",
            "summary": "This table lists the scheduled meeting times and assigned instructors for this class..",
        })

        for time in times:
            split_up = [x.text for x in time.findAll("td")]
            instructor = split_up[6].split('(')[0]
            instructor = re.sub(' +', ' ', instructor).strip()
            if instructor != "TBA":
                dets[1].add(instructor)

        search = r"""<span class="fieldlabeltext">Attributes: </span>(.*?)\n<br/>"""
        attribute = re.search(search, str(full_soup))
        tmp = attribute.group(1).strip() if attribute != None else ""
        if 'Communication Intensive' in tmp:
            dets[0] = True
            
    return dets

async def scrape_CI(years, folder_path):

    for year in tqdm(years):
        f1 = open(folder_path + year + '/courses.json', 'r')
        courses = json.load(f1)
        f1.close()
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=5)) as session:
            for course in courses:
                dets = await get_details(courses[course]['ID'], courses[course]['subj'], year, session)
                courses[course]['properties']['CI'] = dets[0]

                courses[course]['professors'] = list(dets[1])
        f2 = open(folder_path + year + '/courses.json', 'w')
        json.dump(courses, f2, sort_keys=True, indent=2, ensure_ascii=False)
        f2.close()

