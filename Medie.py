import calendar
import csv
import random
from worker_file import Worker
from calendar_file import Calendar


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

        Function calls: None

        """
        self.name = name
        self.nr_of_shifts = shifts_value
        self.calendars = dict()
        self.paramedics = dict()
        self.assistants = dict()
        self.unavailable = dict()
        self.populate()

    def get_name(self):
        return self.name

    def get_nr_of_shifts(self):
        return self.nr_of_shifts

    def get_calendars(self):
        for key, value in self.calendars.items():
            return key

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

    def update_backend(self):
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

    def populate(self):
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

    def show_month_plan(self, month: int, year: int):
        if year in self.calendars:
            year_local = self.calendars[year]
            if month in year_local.months:
                month_local = year_local.months[month]
                month_local.show_days()

    def show_day_plan(self, day: int, month: int, year: int):
        flag = False
        if year in self.calendars:
            year_local = self.calendars[year]
            if month in year_local.months:
                month_local = year_local.months[month]
                if day in month_local.days:
                    day_local = month_local.days[day]
                    day_local.show_shifts()
                    flag = True
        if not flag:
            print("Check again. One of the inputs for the date is wrong.")

    def assign_week(self) -> list:
        """
        Description: This function returns a list of 3 items containing a dictionary, a list and another list. The
        dictionary has keys which are the shifts of string type, and values are list of tuple pairs representing the
        pairs of workers assigned to the shift like this {"K3": [("worker name", worker_object),("worker name",
        worker_object)]}. The first list is a list of tuples that has string - worker_object pairs representing the
        workers that have remained to be manually assigned. The last list contains tuples of string - worker_object
        pairs that represent the unavailable workers.

        Args: None

        Returns: result - Type: list - A list that contains 3 items. A dictionary, a list and a list (read description)

        """
        #make a plan for the week of paramedics and assistants assigned to the daily shifts
        weekly_plan = dict()
        paramedics = list(self.paramedics.items())
        assistants = list(self.assistants.items())
        random.shuffle(paramedics)
        random.shuffle(assistants)
        shifts_nr = self.nr_of_shifts
        for reps in range(shifts_nr):
            if len(paramedics) != 0:
                local_paramedic = paramedics.pop()
            else:
                local_paramedic = ("None", None)
            if len(assistants) != 0:
                local_assistant = assistants.pop()
            else:
                local_assistant = ("None", None)
            pair = [local_paramedic, local_assistant]
            local_shift = "K" + str(reps + 1)
            weekly_plan[local_shift] = pair
        rest = paramedics + assistants
        result = [weekly_plan, rest]
        return result

    def assign_month_shifts(self, month_number: int, year_number: int):
        weeks_of_month = calendar.monthcalendar(year_number, month_number)
        for week in weeks_of_month:
            week_plan = self.assign_week()
            for day in week:
                if day != 0:
                    day_object = self.access_day(day, month_number, year_number)
                    if day_object.get_day_name() == "Saturday" or day_object.get_day_name() == "Sunday":
                        day_object.shifts["K1"] = None
                        day_object.shifts["K2"] = None
                        continue
                    else:
                        day_object.shifts = week_plan[0]
                        day_object.rest = week_plan[1]
                else:
                    continue

    def assign_manually(self, day: int, month: int, year: int, shift: str):
        local_day = self.access_day(day, month, year)
        local_day

    def access_month(self, month_number: int, year_number: int) -> object:
        local_calendar: Calendar = self.calendars[year_number]
        local_month: object = local_calendar.months[month_number]
        return local_month

    def access_day(self, day_number: int, month_number: int, year_number: int) -> object:
        local_calendar: Calendar = self.calendars[year_number]
        local_month: object = local_calendar.months[month_number]
        local_day: object = local_month.days[day_number]
        return local_day
