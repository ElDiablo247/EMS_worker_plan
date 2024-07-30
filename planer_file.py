from Medie import *

kuppenheim = Medie("Medie Kuppenheim", 5)
kuppenheim.add_calendar(2024)
kuppenheim.assign_month_shifts(8, 2024)
august = kuppenheim.access_month(8, 2024)
august.show_plan_by_day()
day = kuppenheim.access_day(30, 8, 2024)
day.show_shifts()
august.show_plan_by_day()
day.assign_rest()
august.show_plan_by_day()