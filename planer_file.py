from Medie import *

kuppenheim = Medie("Medie Kuppenheim", 5)
kuppenheim.add_calendar(2024)
variab = kuppenheim.assign_week()
print(variab)
kuppenheim.assign_month_shifts(8, 2024)
kuppenheim.show_month_plan(8, 2024)