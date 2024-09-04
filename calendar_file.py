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
        self.populate_months()
        self.create_calendar_folder()

    def get_name(self):
        """
        Description: Getter method for the name attribute

        Args: -

        Returns: The name attribute of the Calendar object of type string

        """
        return self.name

    def get_year(self):
        """
        Description: Getter method for the year attribute of a Calendar object

        Args: -

        Returns: The year attribute of the Calendar object of type integer

        """
        return self.year

    def show_months(self):
        """
        Description: Function that shows the months of a Calendar object contained in the months attribute

        Args: -

        Returns: -

        """
        for key in self.months:
            print(key)

    def populate_months(self):
        """
        Description: Function that assigns a Month instance object to each of the month numbers

        Args: -

        Returns: -

        """
        months_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for month in months_list:
            self.months[month] = Month(month, self.get_year())

    def create_calendar_folder(self):
        """
        Description: Function that creates a new folder for a Calendar object and populates it with additional month
        folders and then each month folder with days csv files that represent the days of that month containing the
        day's plan

        Args: -

        Returns: -

        """
        # Define the folder name based on the year
        year_folder = f"{self.year}_Calendar"

        # Create the folder if it does not already exist
        if not os.path.exists(year_folder):
            os.makedirs(year_folder)
            print(f"Folder created: {year_folder}")
        else:
            print(f"Folder already exists: {year_folder}")

        # Create a folder for each month and a file for each day within it
        for month_number, month_object in self.months.items():
            # Define the month folder path using the month name
            month_folder = os.path.join(year_folder, month_object.get_name())

            # Create the month folder if it doesn't already exist
            if not os.path.exists(month_folder):
                os.makedirs(month_folder)
                print(f"Month folder created: {month_folder}")
            else:
                print(f"Month folder already exists: {month_folder}")

            # Create a file for each day in the month
            for day_number, day_object in month_object.days.items():
                # Get the day name (e.g., "Monday")
                day_name = day_object.get_day_name()

                # Define the file path for each day, including the day name
                day_filename = os.path.join(month_folder, f"{day_number} - {day_name}.txt")

                # Check if the .txt file for the day already exists
                if not os.path.exists(day_filename):
                    try:
                        with open(day_filename, mode='w') as file:
                            pass  # Create an empty file
                        print(f"Empty .txt file created: {day_filename}")
                    except IOError as e:
                        # Raise an IOError if there is an issue with file operations
                        raise IOError(f"Error creating file {day_filename}: {e}")
                    except Exception as e:
                        # Raise any other exceptions encountered
                        raise RuntimeError(f"Unexpected error occurred with file {day_filename}: {e}")
                else:
                    print(f".txt file already exists: {day_filename}")
