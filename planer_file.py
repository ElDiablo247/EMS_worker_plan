from Medie import *

kuppenheim = Medie("Medie Kuppenheim", 5)
kuppenheim.add_calendar(2024)
kuppenheim.load_month_backend(8, 2024)

august = kuppenheim.access_month(8, 2024)
august.show_plan_by_day()
kuppenheim.assign_manually(30, 8, 2024, "K5", "Raul Birta", "James Jackson")
