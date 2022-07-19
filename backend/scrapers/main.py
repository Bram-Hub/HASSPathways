import courses_scraper
import pathway_scraper
import sis_scraper
import asyncio
import os
import json
from tqdm import tqdm

if __name__ == "__main__":
    years = list(map(lambda x: x[0], courses_scraper.get_catalogs()))
    years = years[:4]
    all_courses = courses_scraper.scrape_courses()

    print("Started scraping CI courses")
    for year in tqdm(years):
        path = '../../frontend/src/data/json/' + str(year)
        try:
            # Make dir if does not already exist
            os.mkdir(path)
        except Exception:
            print(f"Folder for {str(year)} already made")
        f = open(path + '/courses.json', 'w')
        json.dump(all_courses[year], f, sort_keys=True, indent=2, ensure_ascii=False)
        f.close()
        split_years = [year[:4], year[5:]]
        asyncio.run(sis_scraper.scrape_CI(split_years[0], "fall", path + '/courses.json'))
        asyncio.run(sis_scraper.scrape_CI(split_years[1], "spring", path + '/courses.json'))
        asyncio.run(sis_scraper.scrape_CI(split_years[1], "summer", path + '/courses.json'))
    print("Finished scraping CI courses")

    all_pathways = pathway_scraper.scrape_pathways()
    for year in years:
        path = '../../frontend/src/data/json/' + str(year)

        f = open(path + '/pathways.json', 'w')
        json.dump(all_pathways[year], f, sort_keys=True, indent=2, ensure_ascii=True)
        f.close()