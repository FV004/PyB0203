from datetime import datetime as dt
time = input('Enter the time : ')
print(dt.strptime(time,'%m-%d-%Y').date())