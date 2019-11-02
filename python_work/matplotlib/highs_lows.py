import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期和最高气温
filename = 'Python-death_valley_2015.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y/%m/%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    fig = plt.figure(dpi=128, figsize=(8, 5))
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')
    # 设置图形的格式
    title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

