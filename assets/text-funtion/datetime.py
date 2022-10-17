#this is not working


# from datetime import date


# def dateandtime():
#     today = date.today()
#     today = today.strftime("%B %d %Y")
#     print("today's date: ", today)


# dateandtime()

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
