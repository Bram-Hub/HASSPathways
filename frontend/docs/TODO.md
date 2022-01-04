# TODO

## General
- Check accessibility for all pages (contrast, aria labels, etc...)
- Style guide & terminology guide
- Add an actual homepage
    - Give user option to "add pathways from classes" or "choose a pathway"
- Page to add pathways by course

## My Pathways Page
- Better layout
- Select & delete pathways
   - Checkbox to select multiple pathways at once?
   - Edit: redirect to "edit pathway" page
   - Delete: give user a confirmation modal - maybe move "delete" to top so it affects selection instead of an individual pathway
   - View pathway -> redirect to pathway page (eye button)
- Use a FAB to add courses
- Empty state if there are no classes for a pathway (or just remove it?)
- Visualizer: graph of dependencies and potential "routes" one can take through a pathway

## Pathway Page
- Selecting the same course across 2 tabs should select it in both tabs (not needed if tabs are deduplicated)
- View dependencies graph / warn if a course has an unmet dependency?
    - Maybe a warning icon "dependenc(ies) required: ..."

## Breadcrumbs

breadcrumbs clip bottom border of navbar

class breadcrumbs
- move to each page instead of global!!
- also remove padding 0 !important
check text lengths

## Footer
- Link to github page, issue tracker ("Report a Bug"), and documentation

## Dark/light mode
- Navbar and other UI elements should also look good in light mode
- Text contrast in light mode is poor

## Navbar
- The navbar navigation should actually link somewhere

## Dev
- Remove SASS warnings when compiling for the first time
- Make CSS classes BEM compliant (or some other style guide?)
- Move JS helper functions elsewhere

## Data
- Make a new data scraper to get up to date data
- Note that in the current dataset there are some issues:
   - The original project titlecased everything, so AI -> Ai, II -> Ii, TV -> Tv, 21st -> 21St, you get the idea. This needs to be fixed (or the data replaced)
   - Classes are duplicated in different categories, some pathways really only have two tabs to pick classes from, so the original project just duplicated the classes for the last two tabs.
       - Note that whatever implementation is used, we must make it clear to the user what the requirements to complete a pathway is
       - (Maybe a checklist on the side or the top that automatically gets checked off when the user selects enough classes to complete the pathway requirements)
   - If a class is *deleted*, then users that had the class in their pathway should be notified (and potentially offered a list of related alternatives)

## Pages
- Admin page to add, remove and edit courses, pathways and pathway categories


