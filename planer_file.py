from Medie import *

kuppenheim = Medie("Medie Kuppenheim", 5)
kuppenheim.add_calendar(2024)
kuppenheim.load_month_backend(8, 2024)
august = kuppenheim.access_month(8, 2024)
august.show_plan_by_day()
#kuppenheim.remove_helper(30, 8, 2024, "K2", "Raul Birta")
day = kuppenheim.access_day(30, 8, 2024)
day.show_rest()
kuppenheim.show_workers()
kuppenheim.assign_month_shifts(12, 2024)
december = kuppenheim.access_month(12, 2024)
december.update_month_backend()
