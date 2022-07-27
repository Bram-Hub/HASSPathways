import toMaterialStyle from 'material-color-hash';
import { pathwayCategories } from '../data/data.js';

const colors = {};
for (let category of pathwayCategories) {
    let j = 0;
    let currentColor;
    do {
        currentColor = toMaterialStyle(`${category.name.toLowerCase()}${' '.repeat(j)}`).backgroundColor;
        j++;
        
        if (j > 10) break; // Don't try too long
    } while (
        Object.values(colors).includes(currentColor) || // No duplicate colors
        /#([a-fA-F0-9]{2})\1{2}/.test(currentColor) // No grays (boring)
    );
    colors[category.name.toLowerCase()] = currentColor;
}

export default function getColorFromCategry(categoryName) {
    return colors[categoryName.toLowerCase()] || toMaterialStyle(categoryName.toLowerCase()).backgroundColor;
}
