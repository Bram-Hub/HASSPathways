import { modifiers } from '../data/course-modifiers.js'
const stringSimilarity = require('string-similarity');

/**
 * Count number of modifier search matches (ie 'spring')
 * @param {object} clazz
 * @param {string} query Must be lowercase
 * @return {number} matches
 */
function specialModifierMatches(clazz, query) {
    let matches = 0;
    for (const [key, value] of Object.entries(modifiers)) {
        if (value.search.some(v => query.includes(v.toLowerCase())) && clazz.modifiers.includes(key))
            matches++;
    }
    return matches;
}

/**
 * Default sort for 2 classes
 * @param {object} a Class A
 * @param {object} b Class B
 * @return {number} Comparison
 */
function defaultSort(a, b) {
    return a.ID - b.ID;
}

/**
 * Rank how well a class matches a certain query
 * @param {object} clazz
 * @param {Array{string}} processedQuery Query.lower().split(' ') with hypen removed
 * @return {number} Score
 */
function rankClassSearch(clazz, processedQuery) {
    let score = 0;

    // Exact match of PREFIX or ID
    if (processedQuery.includes(clazz.prefix.toLowerCase()))
        score += 10000;
    if (processedQuery.includes(clazz.ID))
        score += 10000;

    // General closeness score
    let query = processedQuery.join(' ');
    score += 1000 * stringSimilarity.compareTwoStrings(query, clazz.name);
    score += 100  * stringSimilarity.compareTwoStrings(query, clazz.description);

    // Check special filters
    score += 100 * specialModifierMatches(clazz, query);

    return score;
}

/**
 * Search a list of classes
 * @param {Array{Object}} classes
 * @param {string} query
 * @return {Array{Object}} filtered classes (by query)
 */
export default function search(classes, query) {
    if (!query) return classes.sort(defaultSort);

    let words = query
        .toLowerCase()
        .replace(/([A-Za-z]{4})-(\d{4})/, '$1 $2') // Remove hypens between PREFIX-ID
        .split(' ')
    let filtered = classes.filter(clazz => {
        if (specialModifierMatches(clazz, query) > 0)
            return true;
        let passingWords = words.filter(word =>
            (`${clazz.name} ${clazz.ID} ${clazz.prefix} ${clazz.description}`)
                .toLowerCase()
                .includes(word));
        // At least 80% of search query must be present
        return passingWords.length > words.length * 0.8;
    });

    return filtered.sort((a, b) => {
        let a_ = rankClassSearch(a, words);
        let b_ = rankClassSearch(b, words);
        if (a_ === b_) return defaultSort(a, b);
        return b_ - a_;
    });
}
