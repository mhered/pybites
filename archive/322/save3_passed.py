from datetime import datetime, date
DAYS_IN_YEAR=365

def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    if day_of_year is None:
        today = date.today()
        start_year= date(today.year, 1, 1)
        day_of_year = (today - start_year).days
    return books_read >= day_of_year*books_goal/DAYS_IN_YEAR
    
