import os
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
        self.populate_calendar_folder()
        self.create_calendar_folder()

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def show_months(self):
        for key in self.months:
            print(key)

    def populate_calendar_folder(self):
        months_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for month in months_list:
            self.months[month] = Month(month, self.get_year())

    def create_calendar_folder(self):
        # Define the folder name based on the year
        folder_name = f"{self.year}_Calendar"
        # Create the folder if it does not already exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder created: {folder_name}")
        else:
            print(f"Folder already exists: {folder_name}")

        for key, value in self.months.items():
            local_name = value.get_name()
            csv_filename = os.path.join(folder_name, f"{local_name}.csv")

            # Check if the CSV file already exists
            if not os.path.exists(csv_filename):
                try:
                    # Create an empty CSV file if it does not exist
                    with open(csv_filename, mode='w', newline='') as file:
                        # No content is written to the file; it's empty
                        pass
                    print(f"Empty CSV file created: {csv_filename}")
                except Exception as e:
                    print(f"Error creating file {csv_filename}: {e}")
            else:
                print(f"CSV file already exists: {csv_filename}")

