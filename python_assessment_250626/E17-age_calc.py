from datetime import date
import calendar

def calculate_age(birthdate, today):
    y = today.year - birthdate.year
    m = today.month - birthdate.month
    d = today.day - birthdate.day

    # If days are negative, borrow from previous month
    if d < 0:
        m -= 1

        # find previous month and year correctly
        if today.month == 1:
            prev_month = 12
            prev_year = today.year - 1
        else:
            prev_month = today.month - 1
            prev_year = today.year

        # get days in previous month
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
        d += days_in_prev_month

    # If months are negative, borrow from years
    if m < 0:
        y -= 1
        m += 12

    return y, m, d


# ✅ Example
birthdate = date(1995, 5, 15)
today = date(2026, 1, 2)

age = calculate_age(birthdate, today)
print(f"Age: {age[0]} years, {age[1]} months, {age[2]} days")