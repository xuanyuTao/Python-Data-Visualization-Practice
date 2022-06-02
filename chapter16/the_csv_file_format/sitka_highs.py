import csv
from datetime import datetime

import matplotlib.pyplot as plt

# filename = 'chapter16/the_csv_file_format/csv_data/sitka_weather_07-2018_simple.csv'
filename = 'chapter16/the_csv_file_format/csv_data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    
    # Get high temperatures from this file.
    # highs = []
    # for row in reader:
    #     high = int(row[5])
    #     highs.append(high)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# print(highs)

plt.style.use('seaborn')
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# Plot the high temperatures.
fig, ax = plt.subplots()
# ax.plot(highs, c='red')
ax.plot(dates, highs, c='red')

# Format plot.
# ax.set_title("2018年7月每日最高温度", fontsize=24)
ax.set_title("2018年每日最高温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("温度（F）", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
