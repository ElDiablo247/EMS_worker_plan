import calendar


class Day_Class:
    """
    Description: This is the Day class which takes care of the relevant information that a specific day object may
    have like the complete date (year number, month number and day number e.g. 20.08.2024), name of the day, the shifts
    of the day, the rest of the workers that are not assigned yet and the unavailable workers.

    Methods:
        1. __innit__ Constructor
        2. get_number
        3. get_month
        4. get_year
        5. get_day_name
        6. assign_day_name
        7. assign_rest
        8. show_shifts
        9. show_rest
        10. show_unavailable

    """

    def __init__(self, day_number: int, month_number: int, year_number: int):
        """
        Description: Constructor of Day object. day_number is the number of the day depending on its date e.g. if the
        date is 27.08.2024 then the day is month_number is the month number, for example for March it is 3 because
        it is the third month. year_number is the year number for example 2024

        Attributes:

            1. day_number - Type: integer - The number of the day object e.g. 20 if the date is 20.08.2024
            2. month_number - Type: integer - The month number the Day object belongs to e.g. 20 for date 20.08.2024
            3. year - Type: integer - The year in which the Day object belongs e.g 2024
            4. day_name - Type: string - Name of the day e.g. Monday (initially set to None until assign_day_name() is
            called)
            5. shifts - Type: dict - A dictionary where the shifts are keys and a pair of tuples are values which
            represent the pair of workers assigned for the shifts. Each tuple has a string-object pair representing
            the name as string and the worker object.
            6. rest - Type: dict - A dictionary where the keys are string names of worker objects, and the values are
            the worker objects themselves. These are workers that have not been assigned yet
            7. unavailable - Type: dict - A dictionary where the keys are string names of worker objects, and the values
            are the worker objects themselves. These are workers that are not available to be assigned in the plan.

        Function calls:
            1. assign_day_name() - This method uses the calendar class of the python library to assign a
            name to a specific day object based on the date e.g. if the date is 27.07.2024 then the Day object gets the
            name Friday

        """
        self.number = day_number
        self.month = month_number
        self.year = year_number
        self.day_name = None
        self.assign_day_name()
        self.shifts = dict()
        self.rest = dict()
        self.unavailable = dict()

    def get_number(self):
        """
        Description: Getter function for the number of the day e.g. for date 20.08.2024 it returns integer 20

        Args: -

        Returns: number attribute of Type int

        """
        return self.number

    def get_month(self):
        """
        Description: Getter function for the number of the month e.g. for date 20.08.2024 it returns integer 8

        Args: -

        Returns: month attribute of Type int

        """
        return self.month

    def get_year(self):
        """
        Description: Getter function for the number of the year e.g. for date 20.08.2024 it returns integer 2024

        Args:

        Returns: year attribute of Type int

        """
        return self.year

    def get_day_name(self):
        """
        Description: Getter function for the name of the day e.g. Monday

        Args: -

        Returns: The day_name attribute of type string

        """
        return self.day_name

    def assign_day_name(self):
        """
        Description: Function that automatically assigns the day_name attribute based on the date which the user inputs
        e.g. The date is 27.09.2024 then by using the integrated calendar library in Python it sets the name to Friday

        Args: -

        Returns: -

        """
        day_index = calendar.weekday(self.get_year(), self.get_month(), self.get_number())
        name = calendar.day_name[day_index]
        self.day_name = name

    def assign_rest(self):
        """
        Description: When the function assign_month_shifts is called, it assigns the workers to shifts and in case there
        are more pairs than shifts, there is a remainder of workers which is stored in the rest attribute.
        This function assigns the rest of the workers that have not been yet assigned to shifts and puts them as helpers
        which means they assist the main team. This function is directly called from inside the assign_month_shifts
        function to assign the remaining of the workers so it is rarely or never explicitly called from the user.

        Args: -

        Returns: -

        """
        local_rest = list(self.rest.items())
        min_length = min(len(local_rest), len(self.shifts))
        for i in range(1, min_length + 1):
            local_shift = "K" + str(i)
            if local_shift in self.shifts:
                local_worker = local_rest.pop()
                self.shifts[local_shift].append(local_worker)
        self.rest = dict(local_rest)

    def show_shifts(self):
        """
        Description: This function prints the shifts of this specific Day object for the user to see and have a
        general image of the current format. This function can be used to extract information such as who works with
        whom, what shifts are there and which is empty, what workers are unavailable etc.

        Args: -

        Returns: -

        """
        print(str(self.number) + "." + str(self.month) + "." + str(self.year) + ":")
        for key, value in self.shifts.items():
            workers_string = ""
            if value is not None:
                for worker in value:
                    workers_string += " - " + worker[0]
                print(key + ": " + workers_string)
            else:
                print(key + ": " + "None")
        print("")

    def show_rest(self):
        """
        Description: Displays unassigned workers by printing the contents of the 'rest' attribute. This attribute
        typically contains workers not currently assigned to shifts. Since the 'assign_rest' method is automatically
        invoked during 'assign_month_shifts', it is uncommon to find workers in 'rest' unless a previously
        unavailable worker has become available again. In such cases, workers are added to 'rest' to make them
        available for assignment.

        Args: -

        Returns: -

        """
        print("These are unassigned workers:")
        for worker in self.rest.items():
            print(worker[0])

    def show_unavailable(self):
        """
        Description: This function shows the user through print statements the workers that are unavailable for
        assignement usually because of sick leaves or holidays.

        Args: -

        Returns: -

        """
        print("These are unavailable workers:")
        for worker in self.unavailable.items():
            print(worker[0])
