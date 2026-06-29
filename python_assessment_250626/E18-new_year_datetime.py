from datetime import datetime

def new_year_datetime(curr_dt:datetime):
    
    new_nxt_dt = datetime(year=curr_dt.year+1, month=1,day=1)
    print(new_nxt_dt,"\n",curr_dt,sep="")

    delta = new_nxt_dt - curr_dt
    print(delta)
    '''
    days = delta.days
    seconds = delta.seconds
    print(days,"\n",seconds,sep="")
'''
    
    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    return days,hours,minutes



current_date = datetime(2026, 1, 2, 7)
#new_year_datetime(current_date)
days , hours, minutes = new_year_datetime(current_date)
print(f"{days} days,{hours} hours,{minutes} minutes")