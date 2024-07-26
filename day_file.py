import calendar


class Day_Class:

    def __init__(self, number: int, month_number: int, year: int):
        self.number = number
        self.month = month_number
        self.year = year
        self.day_name = None
        self.assign_day_name()
        self.shifts = dict()
        self.rest = []
        self.unavailable = []

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
        for shift, pair in self.shifts.items():
            if len(self.rest) != 0:
                local_worker = self.rest.pop()
                pair.append(local_worker)

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
        for worker in self.rest:
            print(worker[0])

    def show_unavailable(self):
        print("These are unavailable workers:")
        for worker in self.unavailable:
            print(worker[0])
