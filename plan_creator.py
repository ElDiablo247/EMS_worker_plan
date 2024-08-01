import calendar
import random
import copy

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
    # make a plan for a whole week of paramedics and assistants assigned to the daily shifts.
    local_weekly_plan = dict()

    # workers are loaded to local lists and then shuffled to be random
    local_paramedics = list(self.paramedics.items())
    local_assistants = list(self.assistants.items())
    random.shuffle(local_paramedics)
    random.shuffle(local_assistants)
    local_shifts_nr = self.nr_of_shifts

    # repeat as many times as the shifts in the specific day to make pairs of paramedics and assistants
    for reps in range(local_shifts_nr):
        if len(local_paramedics) != 0:
            local_paramedic = local_paramedics.pop()
        else:
            local_paramedic = ("None", None)
        if len(local_assistants) != 0:
            local_assistant = local_assistants.pop()
        else:
            local_assistant = ("None", None)
        local_pair = [local_paramedic, local_assistant]
        local_shift = "K" + str(reps + 1)
        local_weekly_plan[local_shift] = local_pair

    # the rest of the workers (if any) that have not been assigned
    local_rest = local_paramedics + local_assistants
    rest_final = dict(local_rest)
    result = [local_weekly_plan, rest_final, self.unavailable]
    return result


def assign_month_shifts(self, month_number: int, year_number: int):
    """
    Description:

    Args:
        1. ?Name? - Type: ? - ?????????descr??????????
        2. ?Name? - Type: ? - ??????????descr?????????

    Returns: -

    """

    if year_number not in self.calendars:
        raise KeyError("The year entered does not exist.")
    if month_number not in self.calendars[year_number].months:
        raise KeyError("The month entered does not exist.")

    weeks_of_month = calendar.monthcalendar(year_number, month_number)
    for week in weeks_of_month:
        week_plan = self.assign_week()
        for day in week:
            if day != 0:
                day_object = self.access_day(day, month_number, year_number)
                if day_object is None:
                    # access_day already printed the error message, so we just return here
                    return
                if day_object.get_day_name() in ["Saturday", "Sunday"]:
                    day_object.shifts["K1"] = None
                    day_object.shifts["K2"] = None
                else:
                    day_object.shifts = copy.deepcopy(week_plan[0])
                    day_object.rest = copy.deepcopy(week_plan[1])
                    day_object.unavailable = copy.deepcopy(week_plan[2])
                day_object.assign_rest()
