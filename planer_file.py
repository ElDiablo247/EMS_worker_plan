from Medie import *

kuppenheim = Medie("Medie Kuppenheim", 5)
kuppenheim.add_calendar(2024)
august = kuppenheim.access_month(8, 2024)
kuppenheim.assign_month_shifts(8, 2024)
kuppenheim.assign_manually(31, 8, 2024, "K1", "Emily Johnson", "Emma White")
august.show_plan_by_day()
kuppenheim.assign_manually(31, 8, 2024, "K2", "Raul Birta", "Mia Clark")
