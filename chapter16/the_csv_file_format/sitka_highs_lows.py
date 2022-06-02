import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'chapter16/the_csv_file_format/csv_data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn')
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# Plot the high and low temperatures.
fig, ax = plt.subplots()
# ax.plot(dates, highs, c='red')
ax.plot(dates, highs, c='red', alpha=0.5)
# ax.plot(dates, lows, c='blue')
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("2018年每日最高温度和最低温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("温度（F）", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
