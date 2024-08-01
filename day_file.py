import calendar


class Day_Class:

    def __init__(self, number: int, month_number: int, year: int):
        self.number = number
        self.month = month_number
        self.year = year
        self.day_name = None
        self.assign_day_name()
        self.shifts = dict()
        self.rest = dict()
        self.unavailable = dict()

    def get_number(self):
        return self.number

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def get_day_name(self):
        return self.day_name

    def assign_day_name(self):
        day_index = calendar.weekday(self.get_year(), self.get_month(), self.get_number())
        name = calendar.day_name[day_index]
        self.day_name = name

    def assign_rest(self):
        local_rest = list(self.rest.items())
        min_length = min(len(local_rest), len(self.shifts))
        for i in range(1, min_length + 1):
            local_shift = "K" + str(i)
            if local_shift in self.shifts:
                local_worker = local_rest.pop()
                self.shifts[local_shift].append(local_worker)
        self.rest = dict(local_rest)

    def show_shifts(self):
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
        print("These are unassigned workers:")
        for worker in self.rest.items():
            print(worker[0])

    def show_unavailable(self):
        print("These are unavailable workers:")
        for worker in self.unavailable.items():
            print(worker[0])
