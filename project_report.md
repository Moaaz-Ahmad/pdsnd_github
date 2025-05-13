# US Bikeshare Data Analysis Project

## Overview

This project analyzes bikeshare data from three major US cities: Chicago, New York City, and Washington. The analysis is performed using a Python script that allows users to interactively explore the data, filter it by city, month, and day, and view various statistics about bikeshare usage.

## Script Structure

The main Python script is organized as follows:

- **CITY_DATA Dictionary:** Maps city names to their corresponding CSV data files.
- **get_filters():** Prompts the user to specify a city, month, and day to analyze. Handles invalid input using loops.
- **load_data(city, month, day):** Loads the data for the selected city and applies filters for the specified month and day. Returns a Pandas DataFrame with the filtered data.
- **time_stats(df):** Calculates and displays statistics on the most frequent times of travel (most common month, day, and start hour).
- **station_stats(df):** Shows the most popular start station, end station, and the most frequent combination of start and end stations for trips.
- **trip_duration_stats(df):** Computes and displays the total and average trip durations.
- **user_stats(df):** Provides statistics on bikeshare users, including user types, gender distribution, and birth year information (where available).
- **main():** The main loop that ties all functions together, allowing the user to restart the analysis with different filters.

## How It Works

1. **User Interaction:** The script starts by greeting the user and asking for input on which city, month, and day to analyze.
2. **Data Loading:** Based on the user's choices, the script loads the appropriate CSV file and filters the data.
3. **Statistical Analysis:** The script computes and displays:
   - The most common times of travel
   - The most popular stations and trip combinations
   - Total and average trip durations
   - User demographics and statistics
4. **Restart Option:** After displaying the results, the user is prompted to restart the analysis with new filters or exit the program.

## Technologies Used
- Python 3
- pandas
- numpy
- time (for measuring computation duration)

## Usage Instructions
1. Place the script and the CSV data files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) in the same directory.
2. Run the script using Python 3:
   ```
   python bikeshare.py
   ```
3. Follow the on-screen prompts to select the city, month, and day for analysis.
4. View the computed statistics and choose whether to restart or exit.

## Conclusion

This script provides an interactive way to explore bikeshare data and gain insights into usage patterns, popular stations, trip durations, and user demographics in major US cities. It demonstrates the use of Python for data analysis and user-driven exploration.
