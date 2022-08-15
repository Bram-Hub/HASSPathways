# HASS Pathways
[![Netlify Status](https://api.netlify.com/api/v1/badges/5f319796-9a6d-4747-9269-c2bd33bbdf72/deploy-status)](https://app.netlify.com/sites/kind-jepsen-8817be/deploys)
[![deployment](https://github.com/Bram-Hub/HASSPathways/actions/workflows/deployment.yml/badge.svg)](https://github.com/Bram-Hub/HASSPathways/actions/workflows/deployment.yml)
#### Project Details
This project was developed to help students navigate through Rensselaer Polytechnic Institute's newly designed HASS (humanities, arts, and social sciences) curriculum--effective for the class of 2023 and beyond--which requires students to take part in an integrated pathway. The HASS Integrative Pathways were created to enhance students' HASS Core curriculum by bringing intentionality and depth to the requirements. The themes of the pathways vary in their intentionality; some are interdisciplinary, while others focus on a single discipline, providing students with significant options for their coursework. In addition to providing a more in-depth focus to the HASS Core, many Integrative Pathways can be transformed into minors with relative ease.
#### Information in regards to the **[goals of the pathways](https://hass.rpi.edu/advising/hass-integrative-pathways "source")** include:
- Improve student curriculum and academic development.
- Simplify the lives of students in terms of satisfying HASS requirements.
- Lead to minor, or even major.

# Administrator Information
#### Admin Portal
(NOT LIVE AS OF 8/14)
1. Go to www.hasspathways.com
2. Navigate to the Admin portal from home page.
3. Log in using RPI RCS login through shibboleth.
4. Any changes you make will be sent to the backend and later deployed.

<s>
    
#### Data Sheet
https://docs.google.com/spreadsheets/d/1w6BNcxYCE54pvCJJWHiEoE9CiMjRrVNKeUArV97qN8w/edit?usp=sharing

#### Automation
1. Head to https://hasspathways.herokuapp.com/admin
2. Login
3. Head to https://hasspathways.herokuapp.com/upload-csv and upload the CSV file
4. Go to this repository's GitHub Actions page
5. Run the automation (it'll run automatically every Sunday @ 12 AM)
</s>

# Developer Information
#### Frontend Setup
- Clone the repository to your computer
- Install Nodejs - https://nodejs.org/en/download/ (Note some developers may have issues using npm commands, you can use nvm to rollback your node version to work for this project)
- Use the terminal navigate to the `/frontend` directory within the repo.
- Type `npm install` into the terminal to install all packages for the repository.
- Once everything is installed (ignore warnings), type `npm run serve`.
- Visit the specified website the console spits out.
- Note you can use `npm run lint` to fix some warnings that are present.


#### Backend Setup
Outdated as of 8/14. 
<s>
- https://github.com/Bram-Hub/CSV-Uploader
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`
- `python3 manage.py createsuperuser` and enter the information (email field can be left empty)
- `python3 manage.py runserver`
</s>

#### Branches/Pull Requests (old)
Outdated as of 8/14.
<s>
To maintain an individual's credibility towards this project and order, we'll be using branches and pull requests. Branches will separate our work from one another preventing each other from overwriting someone's work. Pull requests is more of a formaility before it goes to production. With an active pull request, it tells the other developers part of the team that a feature/issue has been newly created/resolved. Pull requests will be handled by @nishi7409

The ideal format for a branch name in this project is `issueNumber-&-issueNumber/FirstName`
For example, a possible branch name would be called `3-&-16/John`. You'd base your branch off the `all-frontend` or `all-backend` branch depending on what *stack* (frontend or backend) issue you've been assigned. All issues are created with a label assigned to them (if one hasn't been labeled, let the project leader know ASAP).

When you're completely done with your issues that have been assigned to you, push to your specific branch then create a pull request to the your main-stack's branch (`all-frontend` or `all-backend`). If the pull request is approved, you should expect to see your commits made to your stack's main branch **and** your changes should be out on the live production page.
</s>