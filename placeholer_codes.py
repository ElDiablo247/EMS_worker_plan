def assign_day_shift(self, day: int, month: int, year: int):
    year_local = self.calendars[year]
    month_local = year_local.months[month]
    day_local = month_local.days[day]
    result = self.assign_workers()
    day_local.shifts = result[0]
    self.show_day_plan(day, month, year)



paramedics_list = []
        assistants_list = []
        main_pairs = dict()
        unavailable_workers = []
        #filter the paramedics and assistants for workers that are not available
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