def populate_calendar_folder(self):
    months_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for month in months_list:
        self.months[month] = Month(month, self.get_year())


def create_calendar_folder(self):
    # Define the folder name based on the year
    folder_name = f"{self.year}_Calendar"
    # Create the folder if it does not already exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder created: {folder_name}")
    else:
        print(f"Folder already exists: {folder_name}")