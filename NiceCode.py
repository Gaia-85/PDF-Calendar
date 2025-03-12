import calendar
from calendar import weekday, day_name, day_abbr
import locale
from _locale import *
import random
import math
from calendar import Calendar
from fpdf import FPDF
from itertools import repeat
from datetime import datetime
import fpdf
import self
import fontstyle

pdf = FPDF("P", "mm", "A3")
pdf.add_page()

class CalendarPDF(FPDF):
    def __init__(self, firstweekday=2):
        super().__init__()
        # locale.setlocale(locale.LC_ALL, "de_DE")
        # list(calendar.day_abbr)
        self.firstweekday = firstweekday  # 0=Monday, 6= Sunday
        self.columns = 4  # number of columns
        self.lineNumber = 0
        self.dayNumber = 1

    def header(self):
        if self.page_no() == 1:
            self.set_font("Arial", "B", 25)
            self.set_draw_color(0, 80, 180)
            self.set_text_color(220, 50, 50)
            self.cell(200, 10, "Calendar 2025", 0, 1, "C")

    def add_month_calendar(self, year, month, start_day):
        self.set_font("Arial", "U", 20)
        self.set_draw_color(50, 150, 50)
        self.set_text_color(50, 50, 250)

        # Month and year
        month_name = calendar.month_name[month]
        self.cell(200, 10, f"{month_name} {year}", 0, 1, "C")
        self.cell(25, 12, "", 1, 0, "C")
        self.cell(50, 12, "Ana", 1, 0, "C")
        self.cell(50, 12, "Carmen", 1, 0, "C")
        self.cell(50, 12, "Markus", 1, 0, "C")
        self.ln()

        month_cal = calendar.monthcalendar(year, month)
        self.set_font("Arial", "B", 10)

        for i, week in enumerate(month_cal):
            for x, day in enumerate(week):
                if day == 0:
                    continue
                else:
                    self.cell(25, 12, str(day) + ". " + str(day_abbr[x]), 1, 0, "L")
                    self.cell(50, 12, "", 1, 0, "L")
                    self.cell(50, 12, "", 1, 0, "L")
                    self.cell(50, 12, "", 1, 0, "L")
                    self.ln()


if __name__ == "__main__":
    pdf = CalendarPDF()
    year = 2025
    mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_abbr = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

    for month in range(1, 13):
        pdf.add_page()
        pdf.add_month_calendar(year, month, mdays)

    pdf.output("Calendar2025.pdf")
