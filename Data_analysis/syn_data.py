import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# Function to identify if a date is a weekend (Saturday or Sunday)
def is_weekend(date):
    return date.weekday() == 5 or date.weekday() == 6


# Function to identify if a date is neither Monday nor Friday
def is_open_day(date):
    return date.weekday() != 0 and date.weekday() != 4


# Function to generate list of major public holidays in Vietnam
def get_vietnam_holidays(year):
    holidays = [
        f'{year}-01-01',  # New Year's Day
        f'{year}-05-19',  # Ho Chi Minh's Birthday
        f'{year}-09-02',  # National Day
    ]
    return [datetime.strptime(date, '%Y-%m-%d') for date in holidays]


# Generate dates for weekends and holidays in the specified year
def generate_special_dates(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)

    all_dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
    weekends = [date for date in all_dates if is_weekend(date) and is_open_day(date)]
    holidays = get_vietnam_holidays(year)

    # Ensure holidays are not duplicated in weekends and are open days
    holidays = [date for date in holidays if is_open_day(date)]

    special_dates = set(weekends + holidays)

    return sorted(special_dates)


# Function to generate the dataset
def generate_dataset(year):
    special_dates = generate_special_dates(year)

    # Generate data for each date
    data = []
    id_counter = 1
    for date in special_dates:
        if date.month in [1, 5, 9]:  # Increase visitors during months with public holidays
            num_visitors = np.random.randint(150, 300)
        else:
            num_visitors = np.random.randint(50, 150)

        for _ in range(num_visitors):
            age = np.random.randint(10, 80)  # Random age between 10 and 80
            is_foreign = np.random.rand() < 0.35  # 35% chance of being a foreign guest
            data.append([id_counter, is_foreign, age, date.strftime('%Y-%m-%d')])
            id_counter += 1

    # Create DataFrame
    df = pd.DataFrame(data, columns=['id_person', 'is_foreign', 'age', 'date'])
    return df


# Generate the dataset for the year 2024
dataset_2023 = generate_dataset(2023)

# Display the first few rows of the dataset
print(dataset_2023.head())

# Optionally, save to a CSV file
dataset_2023.to_csv('ho_chi_minh_mausoleum_visits_2023.csv', index=False)
