from Medie import *

kuppenheim = Medie("Medie Kuppenheim", 5)
kuppenheim.add_calendar(2024)
kuppenheim.assign_month_shifts(8, 2024)
pair = kuppenheim.create_pair("Emily Johnson", "Andrew Thompson")
kuppenheim.assign_manually(31, 8, 2024, "K2", pair)
pair = kuppenheim.create_pair("Raul Birta", "James Jackson")
