from datetime import datetime, timedelta

def add_business_days(start_date, n):
    current_date = start_date
    added_days = 0

    while added_days < n:
        current_date += timedelta(days=1)
        if current_date.weekday() < 5: 
            added_days += 1

    return current_date


start = datetime(2026, 1, 2)  
result = add_business_days(start, 5)

print(result.strftime("%Y-%m-%d"))