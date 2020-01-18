import csv
import pandas as pd
from datetime import datetime, date, timedelta

count = 0
line = 0
labels = []
final = []
with open(r'D:\Python\FatAcceptance\Overall\Labels.csv') as f:
    reader = csv.reader(f)
    labels = next(reader)
with open(r'D:\Python\FatAcceptance\Overall\WithRetweets.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if line == 0:
            line = 1
            continue
        row.append(labels[count])
        final.append(row)
        count += 1
df = pd.DataFrame(final, columns=['date', 'text', 'label'])
df = df.sort_values(by='date')
df.to_csv(r'D:\Python\FatAcceptance\Overall\Trend.csv', index=False)
start = date(2010, 1, 1)
end = start + timedelta(weeks=1)
weeks = [{'0': 0, '1': 0, '2': 0}]
week = 0
start_year = date(2010, 1, 1)
end_year = date(2011, 1, 1)
years = [{'0': 0, '1': 0, '2': 0}]
year = 0
for index, row in df.iterrows():
    currdate = datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S').date()
    if currdate >= end:
        week += 1
        start += timedelta(weeks=1)
        end += timedelta(weeks=1)
        weeks.append({'0': 0, '1': 0, '2': 0})
    if currdate >= end_year:
        year += 1
        start_year = date((2010 + year), 1, 1)
        end_year = date((2010 + year + 1), 1, 1)
        years.append({'0': 0, '1': 0, '2': 0})
    years[year][row['label']] += 1
    weeks[week][row['label']] += 1
df_weeks = pd.DataFrame(weeks)
df_years = pd.DataFrame(years)
df_weeks.to_csv(
    r'D:\Python\FatAcceptance\Overall\WeeklyTallies.csv', index=False)
df_years.to_csv(
    r'D:\Python\FatAcceptance\Overall\YearlyTallies.csv', index=False)
