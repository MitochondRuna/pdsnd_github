print('Welcome!')
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city = []
city_df = []
month = []
day = []

def start():
    start = input('Press enter to begin')


def city_filter():
    """ get input for city variable
    Input: a city name (as a string) from three options
    Output: city
    """
    city_name = input('Which city would you like to see data for? Chicago, New York City, or Washington? ').title()
    cities = ['Chicago', 'New York City', 'Washington']
    city = []
    while True:
        if city_name.title() in cities:
            print('You chose: ', city_name)
            break
        else:
            print('You may not have spelled that right, please try again')
            city_name = input('Chicago, New York City, or Washington? ')

    city = str(city_name.lower())
    return city


def month_filter():
    """ get input for month filter
    Input: month name as a string
    Output: month as an integer
    """
    confirm_filter = str(input('There are six months of data available. Which month would you like to see data for?\n January, February, March, April, May or June?  ').title())
    months = {'January': 1, 'February': 2, 'March': 3, 'April' : 4, 'May' : 5, 'June' : 6}
    month = []

    while True:
        if confirm_filter in months:
            month = months[confirm_filter]
            break
        elif confirm_filter == 'Cancel':
            month = 0
            break
        else:
            confirm_filter = str(input('Please try typing the month name again, or type "cancel" to cancel this filter: ').title())
            continue
    return month


def day_filter():
    """ get input for day of the week filter
    Input: day name as a string
    Output: a weekday name as a string
    """
    confirm_filter = str(input('You can select any single weekday. Which day would you like to see data for?\n  ').title())
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day = []
    while True:
        if confirm_filter in days :
            day = confirm_filter
            break
        elif confirm_filter == 'Cancel' :
            day = 0
            break
        else:
            confirm_filter = str(input('Please try typing the full day of the week, e.g. "Sunday" or "Monday", or write "cancel" to cancel this filter  ').title())
            continue
    return day


def next_5(city_df):
    """ take and print next five rows of DataFrame
    Input: none
    Output: next five rows of data from the filtered data set
    """
    num_string = [0,1,2,3,4]
    print(city_df.take(num_string, axis=0))
    x = 5
    while True:
        response = input('Do you want to see the next 5 lines of individual trip data? y/n')
        if response == 'y':
            print_nums = [i+x for i in num_string]
            print(city_df.take(print_nums))
            x += 5
        else:
            break


def get_data(city_df, city, month, day):
    """ get user input to display data output as raw data or summary statistics
    Input: from options, as a string
    Output: data from city_df DataFrame
    """


    print('\nData time!\n', '-'*30, '\nYou can begin viewing your data below, but first you must make a choice:')
    while True:
        response = str(input('If you would like to see the raw trip data, type: "raw" \nOtherwise, if you would prefer to see the summary statistics, type: "stats"  \nTo exit, or change this selection, type: "exit"  ').lower())
        if response == 'raw':
            print('\n')
            print('-'*60,'\nSingle trip data for: {}, month: {}, day of week: {} '.format(city, month, day))
            print('-'*60)
            next_5(city_df)

        elif response == 'stats':
            print('\n')
            print('-'*60,'\nSummary stats for: {}, month: {}, day of week: {} '.format(city, month, day))

            print('-'*60, '\n-- Popular travel times -- ')
            while True:
                if month == 0:
                    pop_month = city_df['month'].mode()[0]
                    month_key = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
                    print('Popular month: ', month_key[pop_month])
                    break
                else:
                    break
            while True:
                if day == 0:
                    print('Popular day: ', city_df['day_of_week'].mode()[0])
                    break
                else:
                    break

            city_df['Start Hour'] = city_df['Start Time'].dt.hour
            print('Starting hour: ', city_df['Start Hour'].mode()[0],':00 hrs')

            print('-'*10, '\n-- Trip info -- ')
            print('Total number of trips: ', city_df['Trip Duration'].count())
            print('Total length of all trips taken: ', (((city_df['Trip Duration'].sum())/60)/60).round(1), 'hours')
            print('Average trip length: ', ((city_df['Trip Duration'].mean())/60).round(1), 'minutes' )
            print('Shortest trip length: ', ((city_df['Trip Duration'].min())/60).round(1), 'minutes')
            print('Longest trip length: ', ((city_df['Trip Duration'].max())/60).round(1), 'minutes')


            print('-'*10, '\n-- Popular station --')
            city_df['Whole Trip'] = city_df[['Start Station','End Station']].agg(' to '.join, axis=1)
            print('Start: ', str(city_df['Start Station'].mode()[0]))
            print('End: ', str(city_df['End Station'].mode()[0]))
            print('Whole trip: ', city_df['Whole Trip'].mode()[0])

            while True:
                print('-'*10, '\n-- Customer details -- \n')
                print('User distribution :\n', city_df['User Type'].value_counts())

                if city == 'chicago' or city == 'new york city':
                    print('\nAverage customer age: ', 2017 - (city_df['Birth Year'].mean().round(1)))
                    print('Oldest customer age: ', int(2017 - (city_df['Birth Year'].min())))
                    print('Youngest customer age: ', int(2017 - (city_df['Birth Year'].max())))
                    print('\nGender:\n', city_df['Gender'].value_counts())
                    break
                elif city == 'washington':
                    print('\n- Note: Age and gender info not available for Washington data -')
                    break
                else:
                    break

            break
        elif response == 'exit':
            break
        else:
             continue
    return city_df


def reset_city(city):
    """ get user input to confirm or change filter settings, then run get_data() again
    Input: Y/N to change city, month and day
    Output: city, month, day - updated
    """

    while True:
        city_response = input('Would you like to change the city? Y/N  ').lower()
        if city_response == 'y':
            city = city_filter()
            break
        else:
            break
    city = str(city.lower())
    return city

def reset_month(month):

    while True:
        month_response = input('Would you like to change the month? Y/N  ').lower()
        if month_response == 'y' or month_response == 'yes':
            month = month_filter()
            break
        else:
            break

    return month

def reset_day(day):
    while True:
        day_response = input('Would you like to change the weekday? Y/N  ').lower()
        if day_response == 'y':
            day = day_filter()
            break
        else:
            break
    return day

def review_data(city_df, city, month, day):
    while True:
        print('-'*60)
        continue_results = str(input('\nIf you would like to choose another data viewing option for this same data, please type: "view" \nIf you would like to reset the data filters, please type: "reset" \nIf you would like to exit the program, just type: "exit".  ').lower())
        if continue_results == 'view':
            get_data(city_df, city, month, day)
            continue
        elif continue_results == 'reset':
            city = reset_city(city)
            city_df = pd.read_csv(CITY_DATA[city])
            month = reset_month(month)
            day = reset_day(day)
            city_df['Start Time'] = pd.to_datetime(city_df['Start Time'])
            city_df['month'] = city_df['Start Time'].dt.month
            city_df['day_of_week'] = city_df['Start Time'].dt.weekday_name
            if month != 0:
                city_df = city_df[city_df['month'] == month]
            if day != 0:
                city_df = city_df[city_df['day_of_week'] == day]
            print('-'*10, '\nYour selection is now set to: {}, month: {}, day: {} '.format(city, month, day))
            get_data(city_df, city, month, day)
            continue
        elif continue_results == 'exit':
            break
        else:
            print('\nYour input didn\'t quite work, please try again.')
            continue


def main():
# Get filters and load the dataframe
    city = city_filter()
    city_df = pd.read_csv(CITY_DATA[city])
    print('Here is a preview of the data: ')
    print(city_df.head())


    print('-'*30,'\nYou can choose to filter this data by a particular month and/or weekday. \nIf you do not set a filter for either of these values they will automatically be set to 0. You can then move on to see the data below.')

    while True:
        confirm_month_filter = str(input('Firstly, would you like to see data for a particular month? Y/N  ').lower())
        if confirm_month_filter == 'y' or confirm_month_filter == 'yes':
            month = month_filter()
            break
        elif confirm_month_filter == 'n' or confirm_month_filter == 'no':
            print('-- No month filter has been set')
            month = 0
            break
        else:
            print('Oops, that didn\'t work properly, please try again by typing "y" or "n"')
            continue

    while True:
        confirm_day_filter = str(input('Would you like to filter data by day of the week? Y/N ').lower())
        if confirm_day_filter == 'y' or confirm_day_filter == 'yes':
            day = day_filter()
            break
        elif confirm_day_filter == 'n' or confirm_day_filter == 'no':
            print('-- No weekday filter has been set')
            day = 0
            break
        else:
            print('Oops, that didn\'t work properly, please try again by typing "y" or "n"')
            continue

    print('\nYou have opted to see data for: {}, for month: {}, and day: {}. Now let\'s view this data! '.format(city, month, day))
    start()

    city_df['Start Time'] = pd.to_datetime(city_df['Start Time'])
    city_df['month'] = city_df['Start Time'].dt.month
    city_df['day_of_week'] = city_df['Start Time'].dt.weekday_name
    if month != 0:
        city_df = city_df[city_df['month'] == month]
    if day != 0:
        city_df = city_df[city_df['day_of_week'] == day]

# city_df moved from here
    get_data(city_df, city, month, day)

    review_data(city_df, city, month, day)


# Intro text
print('\n','-'*10, '\nThis program will help you explore the US BikeShare project data collected in 2017.')
print(' Data is available for three cities across the USA: Chicago, New York City, and Washington.')
print(' After picking a city, you will have the option to filter data based on months or days of the week.')
print(' You will then have the option to view the raw trip data, or view some summary statistics for the data.')
print(' This program also allows you to reset the filters after you have viewed the data.\n', '-'*10)
start()

if __name__ == "__main__":
    main()

print('\nAll done! Thank you for exploring this data today!')    
