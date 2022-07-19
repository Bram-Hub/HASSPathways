#!/usr/bin/env python3

from bs4 import BeautifulSoup
import re

PASSED = {"A", "A-",
        "B+", "B", "B-",
        "C+", "C", "C-",
        "D+", "D",
        "P", "IP", "S", "Z", "NE**"}

FAILED_CODES = {"F", "I", "W", "AU", "U", "FA", "NC", "WI"}

class Course:
    def __init__(self, subj, ID, class_name):
        self.subj = subj
        self.ID = ID
        self.class_name = class_name
    def __eq__(self, other):
        # defined so we can have a set of these objects and take care of cases
        # where people take the class twice (for a better grade for example)
        return (
            self.subj == other.subj and \
            self.ID == other.ID and \
            self.class_name == other.class_name )
    def __str__(self):
        return f"{self.subj} {self.ID} - {self.class_name}"
    def __hash__(self):
        return hash(self.subj + self.ID + self.class_name)
    def __repr__(self): return self.__str__()


def passed_class(grade):
    # see the back of an official transcript for this rubric Decided to count in
    # progress courses, satisfactory coruses, grade unknown, and not examined
    # types to be a pass
    if grade in PASSED: return True
    else: return False

def parse_prev_classes(html):
    soup = BeautifulSoup(html, features = 'html.parser')
    elements = soup.find_all("td", {"class": "dddefault"})

    taken_courses = set()
    index = 0
    while index < len(elements):
        text = elements[index].text.strip()

        if re.search("[A-Z][A-Z][A-Z][A-Z]", text) is not None:
            subj = text
            ID                 = elements[index + 1].text.strip()
            class_type         = elements[index + 2].text.strip() # Should be UG
            class_name         = elements[index + 3].text.strip() # in all caps
            grade              = elements[index + 4].text.strip() # in all caps
            total_credit_hours = elements[index + 5].text.strip() # in all caps
            quality_points     = elements[index + 6].text.strip() # in all caps
            if passed_class(grade): taken_courses.add(Course(subj, ID, class_name))

            index += 7
            continue

        index += 1
    return taken_courses

def parse_classes(html, sem_type):
    soup = BeautifulSoup(html, features = 'html.parser')
    elements = soup.find_all("td", {"class": "dddefault"})

    taken_courses = set()
    index = 0
    while index < len(elements):
        text = elements[index].text.strip()

        if re.search("[A-Z][A-Z][A-Z][A-Z]", text) is not None:
            subj = text
            ID                 = elements[index + 1].text.strip()
            class_type         = elements[index + 2].text.strip() # Should be UG
            class_name         = elements[index + 3].text.strip() # in all caps
            if sem_type == "PREVIOUS":
                grade              = elements[index + 4].text.strip() # in all caps
                total_credit_hours = elements[index + 5].text.strip() # in all caps
                quality_points     = elements[index + 6].text.strip() # in all caps
                if passed_class(grade): taken_courses.add(Course(subj, ID, class_name))
                index += 7
            elif sem_type == "CURRENT":
                # We are going to assume that the student is going to pass all their classes
                taken_courses.add(Course(subj, ID, class_name))
                index += 4
            else: raise Exception("Invalid argument passed to parse_classes(html, sem_type). sem_type can be one of: \"PREVIOUS\" or \"CURRENT\"")

            continue

        index += 1
    return taken_courses

def parse_transcript(path):
    contents = ""
    with open(path) as f:
        contents = f.read()
    rpi_transcript = contents.split("INSTITUTION CREDIT")[1]
    taken_courses = set()
    if re.search("COURSES IN PROGRESS", rpi_transcript): # student is currently taking classes
        prev_classes, current_classes = rpi_transcript.split("COURSES IN PROGRESS")
        taken_courses = taken_courses | parse_classes(prev_classes, "PREVIOUS")
        taken_courses = taken_courses | parse_classes(current_classes, "CURRENT")
    else:
        taken_courses = taken_courses | parse_classes(prev_classes, "PREVIOUS")
    print(taken_courses)


if __name__ == '__main__':
    parse_transcript("./academic_transcipt.html")
