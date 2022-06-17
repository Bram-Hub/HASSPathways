import json
import requests
from bs4 import BeautifulSoup

# finds the pathway name using beautiful soup's .find
def parse_name(page):
    p = page.find("h1")
    return p.get_text().strip()

def parse_courses(tag):
    courses = {}
    for a in tag.find_all("li"):
        txt = a.get_text()
        if txt != 'or' and len(txt) > 0 and txt[0] != '(':
            # fixes all weird unicode and stuff
            course = (txt.strip()
                .replace('\u2013', '-')
                .replace('\u00a0', ' ')
                .replace('\u200b', ''))

            f = open("courses.json")
            all_courses = json.load(f)

            if "Credit Hours" in course:
                course = course[:-15].strip()
            if "-level" in course:
                # add multiple 'blank' level courses from X
                index = course.index("-level")
                level = course[index-4:index]
                subj = course[index+7:index+11]
                for c in all_courses:
                    ID = all_courses[c]["ID"]
                    a_subj = all_courses[c]["subj"]
                    if ID[0] == level[0] and a_subj == subj:
                        courses[c] = subj+ID
            elif "Elective" in course:
                subj = course[:4]
                level = course[5:9]
                for c in all_courses:
                    ID = all_courses[c]["ID"]
                    a_subj = all_courses[c]["subj"]
                    if ID[0] == level[0] and a_subj == subj:
                        courses[c] = subj+ID
            else:
                course_name = course[9:].strip()
                course_code = course[:9].strip().replace(' ', '')
                if "-" in course_name:
                    course_name = course_name[course_name.index("-")+1:].strip()
                courses[course_name] = course_code
    return courses

# finds all body text for the pathway and grabs the courses for each
def parse_body(page):
    name = parse_name(page)
    
    body = {}
    body["name"] = name
    body["description"] = page.find_all("p")[4].get_text()
    for tag in page.find_all("div", "acalog-core"):
        header = tag.find_all("h2")
        if len(header) == 0:
            header = tag.find_all("h3")
            
        header = header[0].get_text()
        if header == "Required:":
            temp = parse_courses(tag)
            body["required"] = temp
        elif header == "Choose one of the following:":
            temp = parse_courses(tag)
            body["one_of"] = temp
        elif "compatible minor" in header.lower():
            temp = set()
            for a in tag.find_all("a"):
                txt = a.get_text()
                if len(txt) > 0 and txt[0] != '(':
                    temp.add(txt.strip())
            for a in tag.find_all("li"):
                txt = a.get_text()
                if len(txt) > 0 and txt[0] != '(':
                    temp.add(txt.strip())
            for a in tag.find_all("p"):
                txt = a.get_text()
                if len(txt) > 0 and txt[0] != '(':
                    temp.add(txt.strip())
            body["minor"] = list(temp)
        else:
            body["remaining_header"] = header
            temp = parse_courses(tag)
            body["remaining"] = temp

    return body

def get_soup(i):
    baseURL = "http://catalog.rpi.edu/preview_program.php?catoid=22&poid="
    r = requests.get(baseURL + str(i), headers={"User-Agent": "Mozilla"})
    soup = BeautifulSoup(r.text, features="html.parser")
    return soup


# should generate a beautiful soup of every pathway page
# the #'s after poid are the page number for the pathways which were manually found
# do note these numbers might change and are temporary
def fetch_webpages():
    all_pages = []

    for i in range(5539, 5561):
        all_pages.append(get_soup(i))

    for i in range(5562, 5585):
        all_pages.append(get_soup(i))

    i = 5596
    all_pages.append(get_soup(i))

    return all_pages

def main():
    print("Starting scraping")
    all_pages = fetch_webpages()
    print("Parsing webpages")
    parsed_pages = {}
    for page in all_pages:
        parsed_pages[parse_name(page)] = parse_body(page)
    print("Creating json")  
    pathways = json.dumps(parsed_pages, indent=4, sort_keys=True)

    jsonFile = open("pathways.json", "w")
    jsonFile.write(pathways)
    jsonFile.close()
    print("Finished")

if __name__ == "__main__":
    main() 