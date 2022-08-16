// import JSSoup from 'jssoup';
let JSSoup = require('jssoup').default;

function format_course_name(name){
  let new_name = name.toLowerCase()
  new_name = new_name.replace(" +", " ")
  new_name = new_name.replace(",", "")
  new_name = new_name.replace("&amp;", "&")

  return new_name
}

function set_union(setA, setB) {
  const _union = new Set(setA);
  for (const elem of setB) {
    _union.add(elem);
  }
  return _union;
}

function passed_class(grade) {

    const PASSED = new Set(["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D",
                      "P", "IP", "S", "Z", "NE**"])
    if(PASSED.has(grade)) return true
    else                  return false

}


function parse_classes(html, sem_type){
  let soup = new JSSoup(html);
  let elements = soup.findAll("td", 'dddefault')

  let taken_courses = new Set()
  let index = 0

  while(index < elements.length){
    const text = elements[index].getText()
    if(!text.search(/^[A-Z][A-Z][A-Z][A-Z]$/)) {
      let subj = text
      let ID                 = elements[index + 1].getText().trim()
      let class_type         = elements[index + 2].getText().trim() // Should be UG
      let class_name         = elements[index + 3].getText().trim() // in all caps
      if(sem_type === "PREVIOUS"){
        let grade              = elements[index + 4].getText().trim() // in all caps
        let total_credit_hours = elements[index + 5].getText().trim() // in all caps
        let quality_points     = elements[index + 6].getText().trim() // in all caps
        if(passed_class(grade)){ taken_courses.add([subj, ID, class_name]) }
        index += 7
      } else if(sem_type == "CURRENT"){
        // We are going to assume that the student is going to pass all their classes
        taken_courses.add([subj, ID, class_name])
        index += 4
      }
      // else: raise Exception("Invalid argument passed to parse_classes(html, sem_type). sem_type can be one of: \"PREVIOUS\" or \"CURRENT\"")
    }
    index += 1
  }
  return taken_courses
}

function get_json_names(toparse, year){
    // SIS displays the names of classes in all CAPS. There are also errors between
    // SIS and the course catalog. There are silly things in the catalog like more
    // than one space between words (open the file and use the following regex to see
    // a couple of them: "  [a-zA-Z]") this will match things as best as possible
    // within the courses.json file. There are some things that aren't cross listed
    // propely within the catalog. Intermediate Logic is one of these.

  ""
  let courses_json = require("../../frontend/src/data/json/" + year + "/courses.json")

    // Store the names and the
  let json_name_lookup = new Map() // stores the lower case version as the key and the name in the json file as the value
  let courses = new Map() // adds all subj-id and lower course names
  for(let json_course_name in courses_json){
    let properties = courses_json[json_course_name]
    json_name_lookup.set(format_course_name(json_course_name), json_course_name)
    json_course_name = format_course_name(json_course_name)
    let subjid = properties["subj"].toUpperCase() + "-" + properties["ID"]
    courses.set(subjid, json_course_name)
    courses.set(json_course_name, subjid)

    properties["cross listed"].forEach((xlisted_subjid) => {
      courses.set(xlisted_subjid, json_course_name)
    })
  }

  let names = []

  // subj, id, name
  toparse.forEach(i => {
    let subjid = i[0] + "-" + i[1] // subj-id
    let name = format_course_name(i[2]) // class name
    if(courses.has(subjid)){
      name = courses.get(subjid)
      names.push(json_name_lookup.get(name))
    } else if(courses.has(name)){
      names.push(json_name_lookup.get(name))
    }
  })
  return names
}

export function parse_transcript(contents, year){
  let rpi_transcript = contents.split("INSTITUTION CREDIT")[1]
  let taken_courses = new Set()

  if(rpi_transcript.search("COURSES IN PROGRESS")){
    let types_of_courses = rpi_transcript.split("COURSES IN PROGRESS")
    let prev_classes = types_of_courses[0]
    let current_classes = types_of_courses[1]
    taken_courses = set_union(taken_courses, parse_classes(prev_classes, "PREVIOUS"))
    taken_courses = set_union(taken_courses, parse_classes(current_classes, "CURRENT"))

  } else {
    taken_courses = set_union(taken_courses, parse_classes(prev_classes, "PREVIOUS"))
  }
  taken_courses = get_json_names(taken_courses, year)
  return taken_courses

}

