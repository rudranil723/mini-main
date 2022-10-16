
from datetime import date


def dateandtime():
    today = date.today()
    today = today.strftime("%B %d %Y")
    print("today's date: ", today)


dateandtime()
