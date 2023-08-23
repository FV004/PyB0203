from datetime import datetime as dt
date_str = input('Enter the date : ')
print(dt.strptime(date_str,'%m-%d-%Y').date())
