from Medie import *

kuppenheim = Medie("Medie Kuppenheim", 5)
kuppenheim.add_calendar(2024)
kuppenheim.assign_month_shifts(6, 2024)
june = kuppenheim.access_month(6, 2024)
june.show_days()
june27 = kuppenheim.access_day(27, 6, 2024)
june27.show_rest()
june27.show_unavailable()
small dick