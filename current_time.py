from datetime import datetime, date
import time

print(datetime.now())
print(datetime.today())

# Get today's date
today = datetime.today().date()

# Create a datetime object for 21:00 on today's date
dt = datetime.combine(today, datetime.strptime("21:00", "%H:%M").time())

print(dt)

while True:
    if datetime.now() > datetime.strptime(f"00:58:50 {date.today()}", "%H:%M:%S %Y-%m-%d"):
        print('Point is passed')
        time.sleep(0.2)
    else:
        print(datetime.now())
        time.sleep(0.2)