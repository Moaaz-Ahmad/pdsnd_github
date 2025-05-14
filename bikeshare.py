import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - city name
        (str) month - month filter
        (str) day - day of the week filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city
    while True:
        city = input("Choose a city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        print("Invalid input. Please enter a valid city name.")

    # get user input for month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Choose a month (January to June) or 'all': ").lower()
        if month in months:
            break
        print("Invalid input. Please enter a valid month.")

    # get user input for day of week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Choose a day of week or 'all': ").lower()
        if day in days:
            break
        print("Invalid input. Please enter a valid day.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """Loads data and filters by month and day."""
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # most common month
    common_month = df['month'].mode()[0].title()
    print('Most Common Month:', common_month)

    # most common day of week
    common_day = df['day_of_week'].mode()[0].title()
    print('Most Common Day of Week:', common_day)

    # most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays stats on the most popular stations and trips."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # most common start station
    print('Most Common Start Station:', df['Start Station'].mode()[0])

    # most common end station
    print('Most Common End Station:', df['End Station'].mode()[0])

    # most common trip
    df['Trip'] = df['Start Station'] + " -> " + df['End Station']
    print('Most Common Trip:', df['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays stats on total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()
    mean_duration = df['Trip Duration'].mean()

    print('Total Travel Time: {:.2f} seconds'.format(total_duration))
    print('Average Travel Time: {:.2f} seconds'.format(mean_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # counts of user types
    print('User Types:\n', df['User Type'].value_counts())

    # counts of gender
    if 'Gender' in df.columns:
        print('\nGender:\n', df['Gender'].value_counts())
    else:
        print('\nGender data not available for this city.')

    # birth year stats
    if 'Birth Year' in df.columns:
        print('\nEarliest Birth Year:', int(df['Birth Year'].min()))
        print('Most Recent Birth Year:', int(df['Birth Year'].max()))
        print('Most Common Birth Year:', int(df['Birth Year'].mode()[0]))
    else:
        print('\nBirth Year data not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
