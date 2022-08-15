import pathwayCategoriesJSON from './json/pathway_categories.json'
import yearsJSON from './json/years.json'

// Neatify JSON data:
// Sort pathways in pathway categories
pathwayCategoriesJSON.forEach(category => category.pathways.sort());

// Prevent accidental modification
Object.freeze(yearsJSON);
Object.freeze(pathwayCategoriesJSON);

export const pathwayCategories = pathwayCategoriesJSON;
export const years = yearsJSON;
