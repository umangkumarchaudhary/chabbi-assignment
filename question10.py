from datetime import datetime, timedelta

def get_previous_date(date, n):
    
    date_obj = datetime.strptime(date, '%y-%m-%d')

    previous_date = date_obj - timedelta(days=n)

    previous_date_str = previous_date.strftime('%y-%m-%d')

    return previous_date_str

date = input("Enter the date (yy-mm-dd): ")
n = int(input("Enter the number of days: "))

previous_date = get_previous_date(date, n)
print(previous_date)
