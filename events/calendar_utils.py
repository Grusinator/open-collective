import calendar
from datetime import date


def month_calendar(year, month):
    cal = calendar.Calendar()
    weeks = cal.monthdatescalendar(year, month)
    return weeks
