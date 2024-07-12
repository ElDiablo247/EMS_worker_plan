
    def filter_unavailable_workers(self) -> list:
        unavailable_workers = []
        paramedics_list = []
        assistants_list = []
        for paramedic_name, paramedic_obj in self.paramedics.items():
            if not paramedic_obj.get_availability_status():
                unavailable_workers.append((paramedic_name, paramedic_obj))
            else:
                paramedics_list.append((paramedic_name, paramedic_obj))
        for assistant_name, assistant_obj in self.assistants.items():
            if not assistant_obj.get_availability_status():
                unavailable_workers.append((assistant_name, assistant_obj))
            else:
                assistants_list.append((assistant_name, assistant_obj))
        random.shuffle(paramedics_list)
        random.shuffle(assistants_list)
        result = [unavailable_workers, paramedics_list, assistants_list]
        return result

    def assign_month_shifts(self, month_number: int, year_number: int):
        local_month = self.access_month(month_number, year_number)
        monday = None
        days_items = list(local_month.days.items())
        # Check if the first day is a weekday and initialize the plan if needed
        first_day_name = days_items[0][1].get_day_name()
        if first_day_name not in ["Saturday", "Sunday"]:
            monday = self.assign_workers()
        for day, day_obj in local_month.days.items():
            if day_obj.get_day_name() == "Saturday":
                continue
            elif day_obj.get_day_name() == "Sunday":
                monday = self.assign_workers()
            else:
                if monday:
                    day_obj.shifts = monday[0]
                    day_obj.rest = monday[1]
                    day_obj.unavailable = monday[2]
                else:
                    print("Wrong")