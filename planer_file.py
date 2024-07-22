from Medie import *

kuppenheim = Medie("Medie Kuppenheim", 5)
kuppenheim.add_calendar(2024)
kuppenheim.assign_month_shifts(8, 2024)
august = kuppenheim.access_month(8, 2024)
first = kuppenheim.access_day(1, 8, 2024)
