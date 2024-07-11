import os

# FILL IN YOUR API_KEY AND USER_ID
params = {
    "API_KEY": "REPLACE THIS (keep quotations)",
    "USER_ID": "REPLACE THIS (keep quotations)"
}

main_file_location = os.path.dirname(__file__)

# By default, the file is expected at "./data/data_long.csv".
# If you need to change the location, modify the path providing
# directories as sequential arguments.
#
# Example for a different location:
# search_info_location = os.path.join(main_file_location, "my_data", "files", "data.csv")  # ./mydata/files/data.csv
search_info_location = os.path.join(main_file_location, "data", "data_long.csv")
