# Practice 16-3: Rainfall Amounts of Sitka

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'practice/csv_file/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and rainfall amounts from this csv data file.
    dates, precips = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        precip = float(row[3])
        precips.append(precip)

# Plot the rainfall amounts.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='blue')

# Format plot.
plt.title("Daily Rainfall Amounts - 2018\nSitka, AK US", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
