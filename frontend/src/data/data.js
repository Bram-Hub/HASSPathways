import coursesJSON  from './json/courses.json'
import pathwaysJSON from './json/pathways.json'
import pathwayCategoriesJSON from './json/pathway_categories.json'

// Neatify JSON data:
// Sort pathways in pathway categories
pathwayCategoriesJSON.forEach(category => category.pathways.sort());

// Add key prop if not already exists
for (let obj of Object.values(coursesJSON))
    if (!obj.key)
        obj.key = obj.prefix + obj.ID;

// Prevent accidental modification
Object.freeze(coursesJSON);
Object.freeze(pathwaysJSON);
Object.freeze(pathwayCategoriesJSON);

export const pathways = pathwaysJSON;
export const pathwayCategories = pathwayCategoriesJSON;
export const courses = coursesJSON;
