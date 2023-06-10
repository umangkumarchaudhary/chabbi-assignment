from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    from_datetime = datetime.strptime(from_date, '%y-%m-%d')
    to_datetime = datetime.strptime(to_date, '%y-%m-%d')

    date_difference = abs((to_datetime - from_datetime).days)

    if date_difference < difference:
        return True
    else:
        return False

from_date = input("Enter the from_date (yy-mm-dd): ")
to_date = input("Enter the to_date (yy-mm-dd): ")
difference = int(input("Enter the difference in days: "))

result = check_date_difference(from_date, to_date, difference)
print(result)
