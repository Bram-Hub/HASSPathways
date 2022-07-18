import courses_scraper
import pathway_scraper
import sis_scraper
import asyncio
import os
import json
if __name__ == "__main__":
    years = list(map(lambda x: x[0], courses_scraper.get_catalogs()))
    years = years[:4]
    CI_file = asyncio.run(sis_scraper.scrape_CI())
    all_courses = courses_scraper.scrape_courses(CI_file)

    for year in years:
        path = '../../frontend/src/data/json/' + str(year)
        try:
            # Make dir if does not already exist
            os.mkdir(path)
        except Exception:
            print(f"Folder for {str(year)} already made")
        f = open(path + '/courses.json', 'w')
        json.dump(all_courses[year], f, sort_keys=True, indent=2, ensure_ascii=False)
        f.close()
    all_pathways = pathway_scraper.scrape_pathways()
    for year in years:
        path = '../../frontend/src/data/json/' + str(year)

        f = open(path + '/pathways.json', 'w')
        json.dump(all_pathways[year], f, sort_keys=True, indent=2, ensure_ascii=False)
        f.close()
    os.remove(CI_file)