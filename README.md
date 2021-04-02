# Covid_Database_Class
Simple Covid Project For Data Analytics Students


## Class outline for students:

### Database Prep
Create a database locally in their personal computer
Load it up manually everyday with new covid statistics pulled from Johns Hopkins' github

### SQL
Students will eventually have their own database of covid data to practice SQL querries

### Data Wrangling
Students can eventually extract information from their own database, perform transformations, joins and analysis on covid data

### Data Visualisation
Students can use transformed data to create visualisations to tell a story and show insights

### Mini Data Project Lifecycle
Revise the entire project, automating it as much as possible so that standard tasks can be performed automatically at any given time

# Getting Started
Set up your database -> The python scripts provided are meant for a local mariadb instance. You'll need to make minor changes to the code to suit your personal needs
Create a database in your mariadb instance called covid (case sensitive)

covid_start.py is the starting script that students will need to initialise their database with all the covid statistical data 
covid_update.py is the script we will have students run once every other day to update their database

Future scripts of the project will be updated as the class progresses
