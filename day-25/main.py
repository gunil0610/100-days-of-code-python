# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(row[1])

# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()

# temp_list = data["temp"].to_list()

# av_temp = sum(temp_list)/len(temp_list)
# print(data["temp"].mean())

# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])

data = pandas.read_csv("Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == 'Gray'])
red_squirrels = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrels = len(data[data["Primary Fur Color"] == 'Black'])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")
