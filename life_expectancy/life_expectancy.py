"""
File Name: life_expectancy.py
Author: Ntyam Adjomo Francky Ludovic

Purpose: write a program to analyze a dataset containing information about life expectancies over the years throughout the countries of the world.

This program also contains a way to Showing Creativity and Exceeding Requirements.
"""
# list where we will add all the value for life expectancy in dataset.
value_life_expectancy = []

# list where we will add all the year in dataset.
year_list = []

# list where we will add all entity in dataset.
entity_list = []

interest_year = int(input("Enter the year or of interest: "))

with open("life_expectancy/life-expectancy.csv") as dataset:
    # Edit our file to remove some unusable data.
    my_new_file = dataset.readlines()

    # We remove the first element to help us to parsing well data.
    my_new_file.pop(0)

    for line in my_new_file:
        line = line.strip()
        parts = line.split(",")
        value_life_expectancy.append(float(parts[3]))
        year_list.append(int(parts[2]))
        entity_list.append(parts[0])

    Max = max(value_life_expectancy)
    Min = min(value_life_expectancy)
    entity_of_max = entity_list[value_life_expectancy.index(Max)]
    entity_of_min = entity_list[value_life_expectancy.index(Min)]
    year_of_max_value = year_list[value_life_expectancy.index(Max)]
    year_of_min_value = year_list[value_life_expectancy.index(Min)]

    print(f"\nThe overall max life expectancy is: {Max} from {entity_of_max} in {year_of_max_value}")
    print(f"The overall min life expectancy is: {Min} from {entity_of_min} in {year_of_min_value}") 

    print(f"\nFor the year {interest_year}")
    interest_year_life_expectancy = []
    total_value = 0
    for index in range(len(year_list)):
        if year_list[index] == interest_year:
            interest_year_life_expectancy.append(value_life_expectancy[index])
            total_value += value_life_expectancy[index]
    average = total_value / len(interest_year_life_expectancy)      
    
    print(f"The average life expectancy across all countries was {round(average, 2)}") 
    print(f"The max life expectancy was in Norway with {max(interest_year_life_expectancy)}")
    print(f"The min life expectancy was in Mali with {min(interest_year_life_expectancy)}")
       