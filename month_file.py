from day_file import *


class Month:
    """
    Description: This class is a category, the month category. Objects of this class are months like February etc.
    The idea is to store all the information like shifts plan of the specific month, in each of these objects. If I
    create an object "December", I can store all the shifts and workers assignments for that month for example
    21 december, shift k1, Alex and Raul. Shift k2, Eva and John.

    Methods:
        1. Constructor
        2. get_name
        3. get_year
        4. get_month_number
        5. get_number_of_days
        6. assign_month_number
        7. assign_number_of_days
        8. populate_month_calendar
        9. add_day
        10. remove_day

    """

    def __init__(self, month: int, year: int):
        """
        Description: Constructor of Month object. Name is the month's name, year is the year of that month, number is
        the month's number in a calendar for example for March it is 3 because it is the third month. Days attribute is
        the most important here because that's where the plan will be stored.

        Attributes:
            1. name - Type: string - Name of month (February)
            2. year - Type: integer - The year in which the month belongs (2024)
            3. month_number - Type: integer - That month's number in the calendar (If February, then 2)
            4. number_of_days - Type: integer - The number of days in that specific month (29, 30 or 31)
            5. days - Type: dict - A dictionary where the dates are keys, and the values will be empty
            dictionaries for later to be edited

        Function calls:
            1. make_plan()
            2.

        """

        self.year = year
        self.month_number = month
        self.number_of_days = 0
        self.assign_number_of_days()
        self.name = ""
        self.assign_month_name()
        self.days = dict()
        self.populate_month_calendar()

    def get_name(self):
        """
        Description: Getter method for the name of the month ("February" for example).

        Args: None

        Returns: The string name attribute of this month object (e.g "March")

        """
        return self.name

    def get_year(self):
        return self.year

    def get_month_number(self):
        return self.month_number

    def get_number_of_days(self):
        return self.number_of_days

    def assign_month_name(self):
        months_dict = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        }
        number = self.get_month_number()
        if number not in months_dict:
            print("Error in the input of the month's number.  " + str(number) + " is not a valid number.")
        else:
            return months_dict[number]

    def assign_number_of_days(self):
        local = calendar.monthrange(self.get_year(), self.get_month_number())[1]
        self.number_of_days = local

    def populate_month_calendar(self):
        """
        Description: This function populates the days dictionary attribute with all the day numbers (1 - 30 for example)
        and each number is an empty key (no values yet)

        Args:
            1. month_number - Type: int - The number of the month (e.g 3 if March, 2 if February etc.)
            2. year_number - Type: int - The year of the month (e.g 2023)

        Returns: None

        """
        local = dict()
        for day in range(1, self.get_number_of_days() + 1):
            local[day] = Day_Class(day, self.get_month_number(), self.get_year())
        self.days = local

    def show_days(self):
        for key, value in self.days.items():
            day_object = value
            day_object.show_shifts()
