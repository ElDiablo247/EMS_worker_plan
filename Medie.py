import csv
import os
import calendar
from worker_file import Worker
from calendar_file import Calendar
from plan_creator import assign_month_shifts, assign_week


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
            2. paramedics - Type: dict - Collection to store string - paramedic_object pairs
            3. assistants - Type: dict - Collection to store string - assistant_object pairs
            4. nr_of_shifts - Type: integer - This is the number of different shifts this medie object has
            5. calendars - Type: dict - This is a dictionary containing the calendars with the plan of the whole year

        Function calls:

            1. populate_workers() - Loads the workers from the backend, to the program's memory.

        """
        self.name = name
        self.nr_of_shifts = shifts_value
        self.calendars = dict()
        self.paramedics = dict()
        self.assistants = dict()
        self.unavailable = dict()
        self.populate_workers()

    def get_name(self):
        return self.name

    def get_nr_of_shifts(self):
        return self.nr_of_shifts

    def get_calendars(self):
        for key, value in self.calendars.items():
            return key

    def get_paramedic(self, paramedic_name: str):
        if paramedic_name in self.paramedics:
            return self.paramedics[paramedic_name]

    def get_assistant(self, assistant_name: str):
        if assistant_name in self.assistants:
            return self.assistants[assistant_name]

    def get_paramedics(self):
        return self.paramedics

    def get_assistants(self):
        return self.assistants

    def change_nr_of_shifts(self, new_number: int):
        self.nr_of_shifts = new_number

    def get_workers(self):
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
        if calendar_year not in self.calendars:
            self.calendars[calendar_year] = Calendar(calendar_year)

    def add_worker(self, obj: Worker):
        """
        Description: User inputs an object Worker, and it is added either to the paramedics dictionary or
        to the assistants dictionary depending on the function of that Worker (only if it does not already exist).
        If a Worker object already exists with the same name attribute as the input, then the user is notified of
        the error.

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
                print("Worker " + worker_name + " already exists in paramedics.")
                return
        elif worker_function == "Assistant":
            if worker_name not in self.assistants:
                self.assistants[worker_name] = obj
                print("Worker " + worker_name + " added to assistants.")
            else:
                print("Worker " + worker_name + " already exists in paramedics.")
                return
        else:
            print("Wrong function. Worker must have function 'Paramedic' or 'Assistant'.")
            return

    def remove_worker(self, name: str):
        """
        Description: User inputs the name attribute of the Worker object which is of type string. The name is
        searched in both paramedics and assistants dictionaries and if found in any of them, the Worker object is
        removed and the user is notified of the change. If the name is not found then the user is also notified that
        the name does not exist.

        Args:
            1. name - Type: string - The name attribute of the Worker object to be removed.

        Returns: -

        """
        if name in self.paramedics:
            removed_worker = self.paramedics.pop(name)
            print("Worker removed: ", removed_worker.get_name())
        elif name in self.assistants:
            removed_worker = self.assistants.pop(name)
            print("Worker removed: ", removed_worker.get_name())
        else:
            print("Worker ", name, " not found in paramedics or assistants.")

    def update_workers_backend(self):
        """
        Description: Changes that are made to the data of the Medie class (all the dictionaries containing workers)
        are also updated to the backend which is a simple text file for simplicity reasons.
        This fuction does exactly that, rereads the date contained in the attributes of a created Medie object, and
        then updates the backend files.
        Function show_workers_txt() is called at the end.

        Args: None

        Returns: -

        """
        with open('Paramedics.txt', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Index', 'Name', 'Function', 'Status'])
            index = 1
            for name, worker in self.paramedics.items():
                writer.writerow([index, name, worker.get_function(), worker.get_availability_status()])
                index += 1
        with open('Assistants.txt', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Index', 'Name', 'Function', 'Status'])
            index = 1
            for name, worker in self.assistants.items():
                writer.writerow([index, name, worker.get_function(), worker.get_availability_status()])
                index += 1
        print("Backend Updated. New context: \n")
        self.populate()

    def populate_workers(self):
        """
        Description: This function is only called from the constructor method once an instance of Medie is created.
        Its purpose is to load the data from the backend, to the storage of the program itself (dictionary
        attributes) so that the user can directly work with the data in hand without having to make a call to the
        backend each time he makes a change The paramedics and assistants dictionaries are loaded with the
        data from the backend txt files.

        Args: None

        Returns: -

        """
        with open('Paramedics.txt', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name = row[1]
                function = row[2]
                availability = row[3]
                availability_status = availability.lower() == 'true'
                paramedic = Worker(name, function, availability_status)
                if paramedic.get_availability_status():
                    self.paramedics[paramedic.get_name()] = paramedic
                else:
                    self.unavailable[paramedic.get_name()] = paramedic
        with open('Assistants.txt', 'r') as file:
            reader2 = csv.reader(file)
            next(reader2)
            for row in reader2:
                name = row[1]
                function = row[2]
                availability = row[3]
                availability_status = availability.lower() == 'true'
                assistant = Worker(name, function, availability_status)
                if assistant.get_availability_status():
                    self.assistants[assistant.get_name()] = assistant
                else:
                    self.unavailable[assistant.get_name()] = assistant
        self.get_workers()

    def show_workers_txt(self):
        """
        Description: This function shows what data the backend contains at the time of calling. Print statements are
        used to show the user the data.

        Args: None

        Returns: -

        """
        with open('Paramedics.txt', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            print("These are our paramedics: ")
            for row in reader:
                print(row[1] + ", " + row[2])
            print(" ")
        with open('Assistants.txt', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            print("These are our medical assistants: ")
            for row in reader:
                print(row[1] + ", " + row[2])

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

        if month_number < 1 or month_number > 12:
            raise ValueError("Invalid month number")

        # Get the month name from the month number
        month_name = calendar.month_name[month_number]
        file_path = os.path.join(f"{year}_Calendar", f"{month_name}.txt")

        if not os.path.exists(file_path):
            print(f"No backend file found for {month_name} {year}.")
            return

        with open(file_path, 'r') as file:
            lines = file.readlines()

        day_number = None
        local_day = None  # Ensure local_day is initialized
        for line in lines:
            line = line.strip()
            if line.startswith("Day:"):
                day_number = int(line.split(":")[1].strip())
                local_day = self.access_day(day_number, month_number, year)
            elif line and day_number is not None and local_day is not None:
                shift_data = line.split(":")
                shift = shift_data[0].strip()
                workers = shift_data[1].strip()
                if workers == "None":
                    local_day.shifts[shift] = None
                else:
                    workers_list = workers.split(", ")
                    paramedics = [(name, self.get_paramedic(name)) for name in workers_list if name in self.paramedics]
                    assistants = [(name, self.get_assistant(name)) for name in workers_list if name in self.assistants]
                    local_day.shifts[shift] = paramedics + assistants
