### Date created
This project was created In July 2020 with the first version completed on
July 7 2020.

### Project Title
Udacity project: US bikeshare data

(aka _Runa's first ever program!_)

### Project Background
This program was created as a project submission requirement for the Udacity
"Programming for Data Science in Python" course.
This submission required the generation of an interactive program using the US bikeshare data provided in three separate csv files.

To complete this task, I used the new skills I had learnt through the course, including example exercises and practice questions.
For some parts of the project I needed some extra assistance and turned to google for help. Any related code I have incorporated into my program has been documented below under "Credits".
This is pretty much my first ever _program_ so I welcome feedback so I may improve in future.

### Program overview
This program provides an environment for a user to navigate the results of the US bikeshare data, provided in 3 csv files (see below).

#### Functionality:
1. The user is prompted to filter data based on a city and a time frame, before moving on to view the data

2. The user is given the option to see either raw data or summary statistics based on the selected filter settings

3. The user is then given the option to go back to choose raw or summary data again; to reset the filter settings; or to exit the program

#### Required files:
main program file:
- bikeshare.py

Data files:
- chicago.csv
- new_york_city.csv
- washington.csv

### Credits
##### Line  147:
    Task: Mode of two columns.
    Source: https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python
    answer by user = silvado
    Code used: `df['period'] = df[['Year', 'quarter', ...]].agg('-'.join, axis=1)`

##### Line  87:
    Task: print 5 lines
    Source: Checked documentation for pandas, use of `.take()`
