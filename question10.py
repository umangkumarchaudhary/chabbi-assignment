from datetime import datetime, timedelta

def get_date_n_days_before(date, n):
    
    date_obj = datetime.strptime(date, '%y-%m-%d')

    
    before_date = date_obj - timedelta(days=n)

    before_date_str = before_date.strftime('%y-%m-%d')

    return before_date_str

date = input("Enter the date (yy-mm-dd): ")

n = int(input("Enter the number of days: "))

result = get_date_n_days_before(date, n)
print("Result:", result)
