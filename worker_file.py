class Worker:
    """
    Description: Class Worker contains and handles data of worker instances. Each Worker object represents one worker.
    The attributes store data such as name, funtion of the worker in the company, the amount of time (hours and minutes)
    he has worked so far in a specific month and his availability status which indicates if he can be considered to be
    planned in for work at a specific given time (a worker would not be available if sick or has an appointment).

    Methods:
        1. Constructor
        2. get_name
        3. get_function
        4. get_working_time
        5. get_availability_status
        6. reverse_availability
        7. set_hours

    """
    def __init__(self, name: str, function: str, availability: bool):
        """
        Description: The user inputs the name, function and availability of a newly created Worker object.

        Attributes:
            1. name - Type: string - The name of a Worker object
            2. function - Type: string - The function of a Worker object (e.g. "Paramedic")
            3. hours - Type: string - The hours a Worker has worked in a specific month
            4. minutes - Type: string - The minutes a Worker has worked in a specific month
            5. availability_status - Type: string - The availability status of a Worker (e.g. available or not available)

        Function calls: None

        """
        self.name = name
        self.function = function
        self.hours = 0
        self.minutes = 0
        self.availability_status = availability

    def get_name(self):
        """
        Description: Getter method for the Worker name attribute.

        Args: None

        Returns: A string representing the name (e.g. "Raul Birta")

        """
        return self.name

    def get_function(self):
        """
        Description: Getter method for the Worker function attribute

        Args: None

        Returns: A string representing the function of a Worker object (e.g. "Paramedic")

        """
        return self.function

    def get_working_time(self):
        """
        Description: Getter method for the working times of a shift.

        Args: None

        Returns: A string representing the amount of time a Worker has worked in this month.
        (e.g. "89 hours and 32 minutes")

        """
        working_time = str(self.hours) + " hours and " + str(self.minutes) + " minutes."
        return working_time

    def get_availability_status(self):
        """
        Description: Getter method for the availability status of a Worker.

        Args: None

        Returns: A boolean indicating True if Worker is available or False if not.

        """
        return self.availability_status

    def reverse_availability(self):
        """
        Description: Setter method for the availabilty status. This method reverses the current status. If True, then it
        reverses to False and vice versa

        Args: None

        Returns: A boolean of the new status.

        """
        self.availability_status = not self.availability_status

    def set_hours(self, change: str, hours_amount: int, minutes_amount: int):
        """
        Description: Setter method of the hours and minutes a Worker has worked. Sometimes changes may be made if a
        Worker has an appointment or worked overtime. If user input is wrong (not + or -) then user is notified.

        Args:
            1. change - Type: string - If "+" then the input time should be added, else if "-" it should be subtracted.
            2. hours_amount - Type: integer - The amount of hours to be added or subtracted from the overall time.
            3. minutes_amount - Type: integer - The amount of minutes to be added or subtracted from the overall time.

        Returns: None

        """
        if change == "+":
            self.hours += hours_amount
            self.minutes += minutes_amount
            if self.minutes >= 60:
                self.hours += 1
                self.minutes -= 60
        elif change == "-":
            self.hours -= hours_amount
            self.minutes -= minutes_amount
            if self.minutes < 0:
                self.hours -= 1
                self.minutes += 60
        else:
            print("Wrong input. Use '+' to add hours or '-' to subtract hours. Also only integers are accepted.")
        print("Current time worked for " + self.get_name() + " is " + self.get_working_time())
