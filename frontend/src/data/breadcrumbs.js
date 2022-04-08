/**
 * Create a breadcrumb obj
 * @param {string} text Label
 * @param {string} href Url
 * @return {object}
 */
function createBreadcrumb(text, href) {
    return { text, href, disabled: false };
}

const HOME = createBreadcrumb('Home', '/');
const PATHWAYS = createBreadcrumb('Pathways', '/pathways');
const MYPATHWAYS = createBreadcrumb('My Pathways', '/my-pathways');
const FROM_CLASSES_SEARCH = createBreadcrumb('Search classes', '/search-classes');
const FROM_CLASSES_PATHWAY = createBreadcrumb('Find classes', '/from-classes');

export default {
    home: [HOME],
    pathways: [HOME, PATHWAYS],
    pathway_template: [HOME, PATHWAYS, null],
    my_pathways: [HOME, MYPATHWAYS],
    my_pathway_template: [HOME, MYPATHWAYS, null],
    from_classes_search: [HOME, FROM_CLASSES_SEARCH],
    from_classes_pathway: [HOME, FROM_CLASSES_SEARCH, FROM_CLASSES_PATHWAY]
};
