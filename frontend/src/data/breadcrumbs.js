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
const FROM_CLASSES_SEARCH = createBreadcrumb('Choose classes', '/choose-classes');
const FROM_CLASSES_PATHWAY = createBreadcrumb('Find classes', '/from-classes');
const ABOUT = createBreadcrumb('About', '/about');
const ADVANCED_SEARCH = createBreadcrumb('Search Classes', '/search-classes');
const ADMIN_HOME_PAGE = createBreadcrumb('Admin Portal', '/admin-portal');
const ADMIN_PATHWAY_PAGE = createBreadcrumb('Pathways Page', '/admin-portal/pathway');
const ADMIN_SEARCH_CC_PAGE = createBreadcrumb('Course Page', '/admin-portal/search-course-code');


export default {
    home: [HOME],
    pathways: [HOME, PATHWAYS],
    pathway_template: [HOME, PATHWAYS, null],
    my_pathways: [HOME, MYPATHWAYS],
    my_pathway_template: [HOME, MYPATHWAYS, null],
    from_classes_search: [HOME, FROM_CLASSES_SEARCH],
    from_classes_pathway: [HOME, FROM_CLASSES_SEARCH, FROM_CLASSES_PATHWAY],
    about_page: [HOME, ABOUT],
    admin_home_page: [HOME, ADMIN_HOME_PAGE],
    admin_course_page: [HOME, ADMIN_HOME_PAGE, null],
    admin_pathway_page: [HOME, ADMIN_HOME_PAGE, ADMIN_PATHWAY_PAGE],
    admin_search_cc_page: [HOME, ADMIN_HOME_PAGE, ADMIN_SEARCH_CC_PAGE],
    advanced_search: [HOME, ADVANCED_SEARCH]
};
