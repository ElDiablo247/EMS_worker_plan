import os
from day_file import *
from backend_functions import update_month_backend


class Month:
    """
    Description: This class is a category, the month category. Objects of this class are months like February etc.
    The days attribute has day objects, for each day of a month. In the day objects it is where work plans are stored,
    but later the plan of each day will be loaded to the attribute month_work_plan when the plan is ready. Basically,
    the reason it is created like this is for modularisation purposes. Days contain shifts, months contain days etc.

    Methods:
        1. __init__ Constructor
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

    def __init__(self, month_number: int, year_number: int):
        """
        Description: Constructor of Month object. month_number is the number, for example for March it is 3 because it
        is the third month. year_number is the number of the year for example 2024

        Attributes:

            1. year - Type: integer - The year in which the month belongs (2024)
            2. month_number - Type: integer - That month's number in the calendar (If February, then 2)
            3. number_of_days - Type: integer - The number of days in that specific month (29, 30 or 31)
            4. name - Type: string - Name of month which is set to "" so it can be assigned from a function call
            5. days - Type: dict - A dictionary where the day numbers are keys, and the values are day objects

        Function calls:
            1. assign_number_of_days() - This function sets the attribute number_of_days using the calendar library
            2. assign_month_name() - This function sets the attribute name using the calendar library
            3. create_days_of_month() - This function creates day objects for each day of this month

        """

        self.year = year_number
        self.month_number = month_number
        self.number_of_days = 0
        self.name = ""
        self.days = dict()
        self.assign_number_of_days()
        self.assign_month_name()
        self.create_days_of_month()

    def get_name(self):
        """
        Description: Getter method for the name of the month ("February" for example).

        Args: None

        Returns: The string name attribute of this month object (e.g "March")

        """
        return self.name

    def get_year(self):
        """
        Description: Getter method for the year in which this Month object belongs e.g. 2024

        Args: -

        Returns: The year of type int

        """
        return self.year

    def get_month_number(self):
        """
        Description: Getter method for the number of this Month object e.g. if this Month is February then 2

        Args: -

        Returns: The number of this Month of type int

        """
        return self.month_number

    def get_number_of_days(self):
        """
        Description: Getter method that returns the number of days that this Month object has e.g. 25

        Args: -

        Returns: An integer that represents the number of days that this Month object has

        """
        return self.number_of_days

    def assign_month_name(self):
        """
        Description: Setter method that sets the name of this Month object. This function is called from the constructor
        and internally further calls the function self.get_month_number() and based on the number of the month, it
        sets the name too e.g. if self.get_month_number() returns 6 then this function sets the name to June because
        it is the 6th month of a calendar.

        Args: -

        Returns: -

        """
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
            self.name = months_dict[number]

    def assign_number_of_days(self):
        local = calendar.monthrange(self.get_year(), self.get_month_number())[1]
        self.number_of_days = local

    def create_days_of_month(self):
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

    def show_plan_by_day(self):
        """
        Description: A function that shows the whole plan of a Month object, by iteratting over each Day object and
        accessing its plan.

        Args: -

        Returns: -

        """
        for day, day_object in self.days.items():
            day_object.show_shifts()

    def update_month_backend(self):
        """
        Description: READ backend_functions.py file the docstring is there

        Args: -

        Returns: -

        """
        return update_month_backend(self)
