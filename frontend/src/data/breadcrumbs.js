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
const PATHWAY_FROM_CLASSES = createBreadcrumb('Find pathway from Classes', '/from-classes');

export default {
    home: [HOME],
    pathways: [HOME, PATHWAYS],
    pathway_template: [HOME, PATHWAYS, null],
    my_pathways: [HOME, MYPATHWAYS],
    my_pathway_template: [HOME, MYPATHWAYS, null],
    pathway_from_classes: [HOME, PATHWAY_FROM_CLASSES]
};
