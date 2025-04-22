import csv
import matplotlib.pyplot as plt

from datetime import datetime

filename = 'sitka_weather_2021_simple.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, highs, lows=[], [], []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[5])
        low = int(row[4])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
print(highs)
print(dates)

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()

