import json

def assemble(path):
    print("Starting category assembler")
    f_years = open(path + 'years.json', 'r')
    years = json.load(f_years)

    all_pathways = {}

    for year in reversed(years):
        f_pathways = open(path + year + '/pathways.json', 'r')
        pathways = json.load(f_pathways)
        for p in pathways:
            all_pathways[p] = pathways[p]

    pairings = {}
    cats = set()
    for p in all_pathways:
        pathway = all_pathways[p]
        subj = {}
        for prio in pathway:
            if prio == 'Remaining' or prio == 'Required':
                for course in pathway[prio]:
                    if pathway[prio][course]:
                        if pathway[prio][course][:4] == 'IHSS':
                            continue
                        if pathway[prio][course][:4] == 'ITWS':
                            subj[pathway[prio][course][:4]] = 9999
                        if pathway[prio][course][:4] in subj:
                            tmp = subj[pathway[prio][course][:4]]
                            subj[pathway[prio][course][:4]] = tmp+1
                        else:
                            subj[pathway[prio][course][:4]] = 1
        subj = sorted(subj.items(), key=lambda item: item[1])
        total = sum(tup[1] for tup in subj)
        tmp = subj[-1][1] / float(total)
        if tmp <= 0.5:
            pairings[p] = 'INTE'
            cats.add('INTE')
        else:
            tmp = subj[-1][0]
            if subj[-1][0] == 'PSYC' or subj[-1][0] == 'PHIL':
                tmp = 'COGS'
            elif subj[-1][0] == 'ITWS' or subj[-1][0] == 'GSAS' or 'Design, Innovation, and Society' in p:
                tmp = 'MAJR'
            elif subj[-1][0] == 'LITR':
                tmp = 'LANG'
            pairings[p] = tmp
            cats.add(tmp)

    subj_to_name = {
        "COMM": "Communication and Media",
        "COGS": "Cognitive Science",
        "ECON": "Economics",
        "ARTS": "Art",
        "INTE": "Interdisciplinary",
        "STSO": "Science and Technology Studies",
        "MAJR": "Major Restricted",
        "LANG": "Language and Literature"
    }

    pathway_cats = {}
    for cat in cats:
        pathway_cats[cat] = {
            'image': cat + '.jpg',
            'name': subj_to_name[cat],
            'pathways': []
        }

    for p in pairings:
        pathway_cats[pairings[p]]['pathways'].append(p)

    pathway_cats = list(sorted(pathway_cats.values(), key=lambda item: item['name']))
    f_out = open(path + 'pathway_categories.json', 'w')
    json.dump(pathway_cats, f_out, sort_keys=True, indent=2, ensure_ascii=False)
    print("Finished category assembler")