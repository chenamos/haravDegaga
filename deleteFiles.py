import os
import csv

# Function to read filenames from the CSV file
def read_filenames_from_csv(csv_file_path):
    filenames = set()
    if os.path.exists(csv_file_path):
        with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)  # Skip the header if present
            for row in reader:
                if row:
                    filenames.add(row[0])
    return filenames

# Specify the path to the folder
folder_path = r"C:\Users\chen\Downloads\takeout-20240822T141127Z-005\Takeout\YouTube ו-YouTube Music\סרטונים"

# Define the CSV file path
csv_file_path = os.path.join(folder_path, "filtered_filenames.csv")

# Read the filenames from the CSV file
filenames_to_keep = read_filenames_from_csv(csv_file_path)

# Get the list of all filenames in the specified folder
all_filenames = os.listdir(folder_path)

# Delete files that are not in the CSV list
for filename in all_filenames:
    if filename not in filenames_to_keep:
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)
        print(f"Deleted: {filename}")

print("Cleanup complete. All files not listed in the CSV have been deleted.")
