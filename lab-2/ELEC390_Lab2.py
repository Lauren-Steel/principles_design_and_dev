# elec 390 assignment 2

# Import statements
import requests
from bs4 import BeautifulSoup

# Making an http request for the following URL
http_text = requests.get("https://weather.com/en-CA/weather/tenday/l/63f4de10a8c7b229661a9674a3d0915b9740827451d381e82b730ca1b96bbbf5").text
soup = BeautifulSoup(http_text, 'lxml')

# Intializing an array to store each day's weather information into one single array.
final_data_array = []

# Scraping weather_data summary
weather_data = soup.find_all('div', class_="DetailsSummary--DetailsSummary--1DqhO DetailsSummary--fadeOnOpen--KnNyF")

# Iterating through the weather_data to find the information needed.
for day in weather_data:
    # Scraping the dates
    date = day.find('h3', class_="DetailsSummary--daypartName--kbngc").text
    
    # Scraping temperature data
    temp_section = day.find('div', class_="DetailsSummary--temperature--1kVVp")
    span_tags = temp_section.find_all('span')

    # To retrieve the maximum temp
    max_temp = span_tags[0].text

    # To retrieve the minimum temp, the ".span.text" goes into the nested span tag, and then would retrieve the contents written in the text.
    min_temp = span_tags[1].span.text
    
    # Scraping weather conditions
    weather_condition = day.find('div', class_="DetailsSummary--condition--2JmHb").span.text
    
    # Scraping chance of precipitation occuring
    chance = day.find('div', class_="DetailsSummary--precip--1a98O").span.text
        
    # Scraping wind speed and direction
    wind_summary = day.find('div', class_="DetailsSummary--wind--1tv7t DetailsSummary--extendedData--307Ax").span.text

    # Spliting the wind speed and direction into seperate entities
    wind_splited = wind_summary.split()
    wind_direction = wind_splited[0]
    wind_speed = wind_splited[1]
        
    # Putting all the information into a final statement to display
    final_summary_data = (date, max_temp, min_temp, weather_condition, chance, wind_direction, wind_speed)
    final_data_array.append(final_summary_data)
    
# Opens a new txt file named 'ELEC390_Lab2' iterates through each of the contents in the final_data_array, converts it into a string, and writes it in the file given its conditions.
with open('ELEC390_Lab2.txt', 'w') as f:
    for i in final_data_array:
          f.write("('" + "', '".join(i) + "')" + "\n")
    