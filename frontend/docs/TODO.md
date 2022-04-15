# TODO

## General
    - Check accessibility for all pages (contrast, aria labels, etc...)
    - Style guide & terminology guide

## My Pathways Page
    - Better layout
    - Select & delete pathways
       - Checkbox to select multiple pathways at once?
       - Delete: Move delete out of part of the ellipsis button
    - Use a FAB to add courses
    - Visualizer: graph of dependencies and potential "routes" one can take through a pathway

## Pathway Page
    - Selecting the same course across 2 tabs should select it in both tabs (not needed if tabs are deduplicated)
    - Change to a graph view

## Breadcrumbs
    -class breadcrumbs
        - move to each page instead of global!!
        - also remove padding 0 !important
        -check text lengths

## Footer
    - Link to github page, issue tracker ("Report a Bug"), and documentation

## Dark/light mode
    - Make both themes better on the eyes

## Dev
    - Remove SASS warnings when compiling for the first time
    - Make CSS classes BEM compliant (or some other style guide?)
    - Move JS helper functions elsewhere

## Data
    - Fix the data files and reformat the JSON
        - Make this not break the website!
    - Make a new data scraper to get up to date data
    - Note that in the current dataset there are some issues:
       - The original project titlecased everything, so AI -> Ai, II -> Ii, TV -> Tv, 21st -> 21St, you get the idea. This needs to be fixed (or the data replaced)
       - Classes are duplicated in different categories, some pathways really only have two tabs to pick classes from, so the original project just duplicated the classes for the last two tabs.
           - Note that whatever implementation is used, we must make it clear to the user what the requirements to complete a pathway is
           - (Maybe a checklist on the side or the top that automatically gets checked off when the user selects enough classes to complete the pathway requirements)
       - If a class is *deleted*, then users that had the class in their pathway should be notified (and potentially offered a list of related alternatives)

## Home
    - Make the home page not horrid

## Style/Cleanup
    - Make the website pretty
    - Cleanup the website for a more user friendly experience

## Pages
    - Admin page to add, remove and edit courses, pathways and pathway categories


## Home page of admin portal
    - Add a course
    - Search by dept
    - Search by course code
    - course page
        - Name
        - dept
        - ID
        - CI
        - HI
        - Description
        - F/S/Summ
        - major restr
        - possible minors
        - pathways it is part of (dropdown)