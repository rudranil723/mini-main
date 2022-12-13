# for now()
import datetime

# for timezone()
import pytz

# using now() to get current time
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

# printing current time in india
print("The current time in india is :", current_time)
