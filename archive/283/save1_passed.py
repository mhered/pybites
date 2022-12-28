from datetime import date, timedelta
def tomorrow(today=None):
    # Your code goes here
    if not today:
        today = date.today()
        
    return today + timedelta(days=1)
    

print(tomorrow(date(year = 1975, month=4, day=8)))