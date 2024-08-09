from calendar_file import Calendar
from plan_creator import assign_month_shifts, assign_week
from backend_functions import *


class Medie:
    """
    Description: Class Medie contains and manipulates the general data of the program. This is the main Class of the
    program. This class behaves like a Databank containing the workers who work for the company, their roles
    (paramedics or assistants), their availability, existing shifts and their operating times and some other data like
    backend files and functions that can manipulate them etc.

    Methods:
        1. Constructor
        2. add_worker
        3. remove_worker
        4. get_length_workers
        5. change_availability
        6. update_backend
        7. populate
        8. show_workers_text

    """

    def __init__(self, name: str, shifts_value: int):
        """
        Description: Constructor method, setting the name of class Medie and the number of shifts it contains.
        Paramedics, assistants and calendars dicts are inititated.

        Attributes:
            1. name - Type: string - Name of the class Medie.
            2. nr_of_shifts - Type: integer - This is the number of different shifts this medie object has
            3. calendars - Type: dict - This is a dictionary containing the calendars with the plan of the whole year
            4. paramedics - Type: dict - Collection to store string - paramedic_object pairs
            5. assistants - Type: dict - Collection to store string - assistant_object pairs
            6. unavailable - Type: dict - Collection to store workers that are not available for planning

        Function calls:

            1. populate_workers() - Loads the workers data from the backend, to the program's memory.

        """
        self.name = name
        self.nr_of_shifts = shifts_value
        self.calendars = dict()
        self.paramedics = dict()
        self.assistants = dict()
        self.unavailable = dict()
        self.populate_workers()

    def get_name(self):
        """
        Description: Getter function to return the name of a Medie object

        Args: -

        Returns: The name of the Medie object.

        """
        return self.name

    def get_nr_of_shifts(self):
        """
        Description: Getter function for the number of shifts of a Medie object

        Args: -

        Returns: A number of type int representing the number of shifts

        """
        return self.nr_of_shifts

    def get_calendar(self, calendar_year: int):
        """
        Description: Getter function that returns the calendar object if it exists

        Args:
            1. calendar_year - Type: int - The calendar year e.g. 2024

        Returns: Calendar object

        """
        if calendar_year in self.calendars:
            return self.calendars[calendar_year]
        else:
            raise KeyError("The number does not exist or there is a typo mistake. Try again")

    def get_paramedic(self, paramedic_name: str):
        """
        Description: Getter function that returns a paramedic object if it exists

        Args:
            1. paramedic_name - Type: string - The string name of the paramedic object. If it exists, it gets returned

        Returns: A paramedic object

        """
        if paramedic_name in self.paramedics:
            return self.paramedics[paramedic_name]
        else:
            raise KeyError("The name does not exist or there is a typo mistake. Try again")

    def get_assistant(self, assistant_name: str):
        """
        Description: Getter function that returns an assistant object if it exists

        Args:
            1. assistant_name - Type: string - The string name of the assistant object. If it exists, it gets returned

        Returns: An assistant object

        """
        if assistant_name in self.assistants:
            return self.assistants[assistant_name]
        else:
            raise KeyError("The name does not exist or there is a typo mistake. Try again")

    def change_nr_of_shifts(self, new_number: int):
        if new_number > 0:
            self.nr_of_shifts = new_number
        else:
            raise ValueError("Number must be higher than 0")

    def show_workers(self):
        """
        Description: A function that shows the user the workers that work for this specific Medie object.

        Args: -

        Returns: -

        """
        paramedics = ["Paramedics and their availabilty\n"]
        for key, paramedic_object in self.paramedics.items():
            name = key
            function = paramedic_object.get_function()
            status = paramedic_object.get_availability_status()
            row = [name, function, status]
            paramedics.append(row)
        for row in paramedics:
            print(row)
        print("")
        assistants = ["Assistants and their availabilty\n"]
        for key, assistant_object in self.assistants.items():
            name = key
            function = assistant_object.get_function()
            status = assistant_object.get_availability_status()
            row = [name, function, status]
            assistants.append(row)
        for row in assistants:
            print(row)
        print("")
        unavailable = ["Unavailable workers\n"]
        for key, worker_object in self.unavailable.items():
            name = key
            function = worker_object.get_function()
            status = worker_object.get_availability_status()
            row = [name, function, status]
            unavailable.append(row)
        for row in unavailable:
            print(row)
        print("")

    def add_calendar(self, calendar_year: int):
        """
        Description: Function that adds a new calendar in the calendars attribute

        Args:
            1. calendar_year - Type: int - The year of the calendar to add e.g. 2023

        Returns: -

        """
        if calendar_year not in self.calendars:
            self.calendars[calendar_year] = Calendar(calendar_year)
        else:
            raise ValueError("Calendar already exists.")

    def add_worker(self, obj: Worker):
        """
        Description: Add new worker based on function (paramedic or assistant) if does not already exist.

        Args:
            1. obj - Type: Worker - The object to be added to the corresponding dictionary.

        Returns: -

        """
        worker_name = obj.get_name()
        worker_function = obj.get_function()
        if worker_function == "Paramedic":
            if worker_name not in self.paramedics:
                self.paramedics[worker_name] = obj
                print("Worker " + worker_name + " added to paramedics.")
            else:
                raise KeyError("Worker already exists in paramedics.")
        elif worker_function == "Assistant":
            if worker_name not in self.assistants:
                self.assistants[worker_name] = obj
                print("Worker " + worker_name + " added to assistants.")
            else:
                raise KeyError("Worker already exists in assistants.")
        else:
            raise KeyError("Wrong function for the worker added. Check again.")

    def remove_worker(self, name: str):
        """
        Description: Worker object to be romoved from the paramedics or assistants attributes if string name exists.

        Args:
            1. name - Type: string - The string name attribute of the Worker object to be removed.

        Returns: -

        """
        if name in self.paramedics:
            removed_worker = self.paramedics.pop(name)
            print("Worker removed: ", removed_worker.get_name())
        elif name in self.assistants:
            removed_worker = self.assistants.pop(name)
            print("Worker removed: ", removed_worker.get_name())
        else:
            raise KeyError("The name entered does not exist.")

    def populate_workers(self):
        return populate_workers(self)

    def show_day_plan(self, day: int, month: int, year: int):
        if year not in self.calendars:
            raise KeyError("Year does not exist.")
        if month not in self.calendars[year].months:
            raise KeyError("Month does not exist.")
        if day not in self.calendars[year].months[month].days:
            raise KeyError("Day does not exist.")

        day_local = self.calendars[year].months[month].days[day]
        day_local.show_shifts()

    def assign_manually(self, day: int, month: int, year: int, shift: str, new_paramedic: str, new_assistant: str):
        local_day = self.access_day(day, month, year)
        if shift not in local_day.shifts:
            raise KeyError("Shift does not exist, or has not been created yet. Try again.")
        if new_paramedic not in self.paramedics:
            raise KeyError("Paramedic does not exist or is unavailable. Try again")
        if new_assistant not in self.assistants:
            raise KeyError("Assistant does not exist or is unavailable. Try again")

        paramedic_tuple = (new_paramedic, self.get_paramedic(new_paramedic))
        assistant_tuple = (new_assistant, self.get_assistant(new_assistant))
        pair = [paramedic_tuple, assistant_tuple]
        local_day.shifts[shift] = pair
        print("Showing the change:")
        local_day.show_shifts()
        self.check_plan(local_day.shifts)

    def check_plan(self, plan: dict):
        flag = True
        local_workers = dict()
        # Check duplicates of workers
        for shift, pair in plan.items():
            for worker in pair:
                if worker[0] not in local_workers:
                    local_workers[worker[0]] = 1
                else:
                    flag = False
                    local_workers[worker[0]] += 1
                    print(worker[0] + " already exists in today's plan. Make some changes.")
                    print("")

        # Check if there are workers that have not been assigned
        for paramedic, paramedic_obj in self.paramedics.items():
            if paramedic not in local_workers:
                flag = False
                print(paramedic + " is not assigned.")
        for assistant, assistant_obj in self.assistants.items():
            if assistant not in local_workers:
                flag = False
                print(assistant + " is not assigned.")
        if flag:
            print("Everything fine")

    def add_helper(self, day: int, month: int, year: int, shift: str, worker_name: str):
        local_day = self.access_day(day, month, year)
        if shift not in local_day.shifts:
            raise KeyError("Shift does not exist.")
        if worker_name in self.paramedics:
            local_tuple = (worker_name, self.paramedics[worker_name])
            if len(local_day.shifts[shift]) == 2:
                local_day.shifts[shift].append(local_tuple)
        elif worker_name in self.assistants:
            local_tuple = (worker_name, self.assistants[worker_name])
            if len(local_day.shifts[shift]) == 2:
                local_day.shifts[shift].append(local_tuple)
        elif worker_name in self.unavailable:
            print("Worker is unavailable and can't be assigned")
            return
        else:
            raise KeyError("Worker does not exist.")

        local_day.show_shifts()
        print(worker_name + " added as helper to the shift " + shift)
        self.check_plan(local_day.shifts)

    def remove_helper(self, day: int, month: int, year: int, shift: str, worker_name: str):
        local_day = self.access_day(day, month, year)
        if shift not in local_day.shifts:
            raise KeyError("Shift does not exist.")
        else:
            local_pair = local_day.shifts[shift]
            if len(local_pair) == 3:
                if local_pair[-1][0] == worker_name:
                    local_pair.pop()
                else:
                    raise KeyError("The entered worker name is wrong")
            else:
                raise ValueError("This shift does not have any helper.")
        local_day.show_shifts()
        print(worker_name + " removed as helper from shift  " + shift)
        self.check_plan(local_day.shifts)

    def access_month(self, month_number: int, year_number: int) -> object:
        if year_number not in self.calendars:
            raise KeyError("Year does not exist. Try again")
        if month_number not in self.calendars[year_number].months:
            raise KeyError("Month does not exist. Try again")

        return self.calendars[year_number].months[month_number]

    def access_day(self, day_number: int, month_number: int, year_number: int) -> object:
        if year_number not in self.calendars:
            raise KeyError("Year does not exist.")
        if month_number not in self.calendars[year_number].months:
            raise KeyError("Month does not exist.")
        if day_number not in self.calendars[year_number].months[month_number].days:
            raise KeyError("Day does not exist.")

        return self.calendars[year_number].months[month_number].days[day_number]

    def assign_month_shifts(self, month_number: int, year_number: int):
        return assign_month_shifts(self, month_number, year_number)

    def assign_week(self) -> list:
        return assign_week(self)

    def load_month_backend(self, month_number: int, year: int):
        return load_month_backend(self, month_number, year)

    def update_workers_backend(self):
        return update_workers_backend(self)

    def show_workers_backend(self):
        return show_workers_backend(self)
