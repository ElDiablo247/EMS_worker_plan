from month_file import Month


class Calendar:
    """
    Description: Calendar objects are basically calendars containing all the plans made in the year and the assignements
    of workers to shifts, shifts to days, days to months. It is the chierarchy of the whole annual plan.

    Methods:
        1. Constructor
        2. get_name
        3. get_year
        4. populate_year_calendar
        5. add_month
        6. remove_month

    """

    def __init__(self, year: int):
        """
        Description: Constructor of class Calendar. User inputs the year of the calendar in integer form. Attributes
        are assigned respectively. The attribute self.months is a dictionary containing string - month_objects pairs
        after populate_calendar_months is executed.

        Attributes:
            1. year - Type: integer - Integer input of user representing the year of the calendar object
            2. name - Type: string - year attribute transformed to string and with concatenation of "Calendar" is
            the name of the object ("2024 Calendar")
            3. months - Type: dictionary - A dictionary containing string - month_objects pairs

        Function calls:
            1. populate_calendar_months()

        """
        self.year = year
        self.name = str(year) + " Calendar"
        self.months = dict()
        self.populate_year_calendar()

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def populate_year_calendar(self):
        months_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for month in months_list:
            self.months[month] = Month(month, self.get_year())

    def show_months(self):
        for key in self.months:
            print(key)

