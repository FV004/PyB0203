from datetime import datetime as dt
date = input('Enter the date : ')
print(dt.strptime(date,'%m-%d-%Y').date())