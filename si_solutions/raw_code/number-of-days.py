from datetime import datetime

def dates(date1, date2):
    date_format = "%Y-%m-%d"
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)
    difference = datetime1 - datetime2
    return abs(difference.days)
date1, date2 = input().split() 
print(dates(date1, date2))