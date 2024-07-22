import os
from day_file import *


class Month:
    """
    Description: This class is a category, the month category. Objects of this class are months like February etc.
    The days attribute has day objects, for each day of a month. In the day objects it is where work plans are stored,
    but later the plan of each day will be loaded to the attribute month_work_plan when the plan is ready. Basically,
    the reason it is created like this is for modularisation purposes. Days contain shifts, months contain days etc.

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
        Description: Constructor of Month object. month is the month number, for example for March it is 3 because it
        is the third month. year is the year number for example 2024

        Attributes:

            1. year - Type: integer - The year in which the month belongs (2024)
            2. month_number - Type: integer - That month's number in the calendar (If February, then 2)
            3. number_of_days - Type: integer - The number of days in that specific month (29, 30 or 31)
            4. name - Type: string - Name of month which is set to "" so it can be assigned from a function call
            5. days - Type: dict - A dictionary where the day numbers are keys, and the values are day objects
            6. month_work_plan - Type: dict - A dictionary containing the finished plan for the month

        Function calls:
            1. assign_number_of_days() - This function sets the attribute number_of_days using the calendar library
            2. assign_month_name() - This function sets the attribute name using the calendar library
            3. create_days_of_month() - This function creates day objects for each day of this month

        """

        self.year = year
        self.month_number = month
        self.number_of_days = 0
        self.assign_number_of_days()
        self.name = ""
        self.assign_month_name()
        self.days = dict()
        self.create_days_of_month()
        self.month_work_plan = dict()

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

    def save_month_plan(self):
        for day, day_object in self.days.items():
            if day not in self.month_work_plan:
                self.month_work_plan[day] = {}
            for shift, pair in day_object.shifts.items():
                if pair is not None:
                    self.month_work_plan[day][shift] = (pair[0][0], pair[1][0])
                else:
                    self.month_work_plan[day][shift] = "None"
        self.show_month_plan()

    def show_month_plan(self):
        for day, shifts in self.month_work_plan.items():
            print(str(day) + " of " + self.get_name())
            for shift, pair in shifts.items():
                print(shift + " -", pair)
            print("")

    def show_plan_by_day(self):
        for day, day_object in self.days.items():
            day_object.show_shifts()

    def update_month_backend(self):
        file_path = os.path.join(f"{self.year}_Calendar", f"{self.get_name()}.txt")
        with open(file_path, 'w') as file:
            for day, day_object in self.days.items():
                file.write(f"Day: {day}\n")
                for shift, pair in day_object.shifts.items():
                    if pair is not None:
                        workers = f"{pair[0][0]}, {pair[1][0]}"
                        file.write(f"Shift {shift}: {workers}\n")
                    else:
                        file.write(f"Shift {shift}: None\n")
                file.write("\n")
