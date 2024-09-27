import os
import calendar
import csv
from worker_file import Worker


def update_month_backend(self):
    """
    Description: Backend is updated with the current data in the system. All changes made will be loaded to the backend
    txt files.

    Args: None

    Returns: -

    """

    # Define the path for the month folder using the month name
    month_folder = os.path.join(f"{self.year}_Calendar", self.get_name())

    # Ensure the month folder exists
    if not os.path.exists(month_folder):
        os.makedirs(month_folder)
        print(f"Month folder created: {month_folder}")

    # Write each day's shifts to a separate file named by the day number and day name
    for day_number, day_object in self.days.items():
        # Get the day name (e.g., "Monday")
        day_name = day_object.get_day_name()

        # Define the file path for each day, including the day name
        file_path = os.path.join(month_folder, f"{day_number} - {day_name}.txt")

        # Write the shift information to the file
        with open(file_path, 'w') as file:
            # Write shift information
            for shift, pair in day_object.shifts.items():
                if pair is not None:
                    # Collect all worker names in a single line, separated by commas
                    workers = ", ".join(worker[0] for worker in pair)
                    file.write(f"{shift}: {workers}\n")
                else:
                    file.write(f"{shift}: None\n")

            # Write rest of the workers
            rest_workers = ", ".join(worker[0] for worker in day_object.rest.items())
            file.write(f"\nRest of workers: {rest_workers if rest_workers else 'None'}\n")

            # Write unavailable workers
            unavailable_workers = ", ".join(worker[0] for worker in day_object.unavailable.items())
            file.write(f"Unavailable workers: {unavailable_workers if unavailable_workers else 'None'}\n")


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
            if not paramedic.get_availability_status():
                self.unavailable[paramedic.get_name()] = paramedic
            self.paramedics[paramedic.get_name()] = paramedic
    with open('Assistants.txt', 'r') as file:
        reader2 = csv.reader(file)
        next(reader2)
        for row in reader2:
            name = row[1]
            function = row[2]
            availability = row[3]
            availability_status = availability.lower() == 'true'
            assistant = Worker(name, function, availability_status)
            if not assistant.get_availability_status():
                self.unavailable[assistant.get_name()] = assistant
            self.assistants[assistant.get_name()] = assistant
    self.show_workers()


def load_month_backend(self, month_number: int, year: int):
    """
    Description: Function that loads the data from the backend to the specific month the user inputs.

    Args:
        1. month_number - Type: int - The number of the month for which to load the data e.g. 1 for January
        2. year - Type: int - The year in which the month belongs

    Returns: -

    """
    if month_number < 1 or month_number > 12:
        raise ValueError("Invalid month number")

    # Get the month name from the month number
    month_name = calendar.month_name[month_number]
    month_folder = os.path.join(f"{year}_Calendar", month_name)

    if not os.path.exists(month_folder):
        print(f"No backend file found for {month_name} {year}.")
        return

    # Iterate over each day's file in the month folder
    for day_file in os.listdir(month_folder):
        file_path = os.path.join(month_folder, day_file)
        day_number = int(day_file.split(' ')[0])  # Extract the day number from the file name
        local_day = self.access_day(day_number, month_number, year)

        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("K"):  # Shift lines start with "K" (e.g., "K1", "K2")
                shift_data = line.split(":")
                shift = shift_data[0].strip()
                workers = shift_data[1].strip()
                if workers == "None":
                    local_day.shifts[shift] = None
                else:
                    workers_list = workers.split(", ")
                    all_workers = []
                    for name in workers_list:
                        if name in self.paramedics:
                            all_workers.append((name, self.get_paramedic(name)))
                        elif name in self.assistants:
                            all_workers.append((name, self.get_assistant(name)))
                        else:
                            # Handle other types of workers if necessary
                            print(f"Warning: Worker '{name}' not found in paramedics or assistants")
                    local_day.shifts[shift] = all_workers

            elif line.startswith("Rest of workers:"):
                rest_data = line.split(":")[1].strip()
                if rest_data != "None":
                    rest_workers_list = rest_data.split(", ")
                    for name in rest_workers_list:
                        if name in self.paramedics:
                            local_day.rest[name] = self.get_paramedic(name)
                        elif name in self.assistants:
                            local_day.rest[name] = self.get_assistant(name)
                        else:
                            print(f"Warning: Rest worker '{name}' not found")

            elif line.startswith("Unavailable workers:"):
                unavailable_data = line.split(":")[1].strip()
                if unavailable_data != "None":
                    unavailable_workers_list = unavailable_data.split(", ")
                    for name in unavailable_workers_list:
                        if name in self.paramedics:
                            local_day.unavailable[name] = self.get_paramedic(name)
                        elif name in self.assistants:
                            local_day.unavailable[name] = self.get_assistant(name)
                        else:
                            print(f"Warning: Unavailable worker '{name}' not found")


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


def show_workers_backend(self):
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