import courseCategoriesJSON from './json/course_categories.json'
import pathwayCategoriesJSON from './json/pathway_categories.json'
import yearsJSON from './json/years.json'

// Neatify JSON data:
// Sort pathways in pathway categories
courseCategoriesJSON.forEach(category => category.courses.sort());
pathwayCategoriesJSON.forEach(category => category.pathways.sort());

// Prevent accidental modification
Object.freeze(yearsJSON);
Object.freeze(pathwayCategoriesJSON);
Object.freeze(courseCategoriesJSON);

export const courseCategories = courseCategoriesJSON;
export const pathwayCategories = pathwayCategoriesJSON;
export const years = yearsJSON;
