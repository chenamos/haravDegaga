import os
import csv

# Function to filter filenames based on a list of expressions
def filter_filenames(filenames, expressions):
    filtered = []
    for filename in filenames:
        if any(expr in filename for expr in expressions):
            filtered.append(filename)
    return filtered

# Function to read and return existing filenames from a CSV file
def read_existing_filenames(csv_file_path):
    existing_filenames = set()
    if os.path.exists(csv_file_path):
        with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)  # Skip the header if present
            for row in reader:
                if row:
                    existing_filenames.add(row[0])
    return existing_filenames

# Specify the root path to the folder
root_folder_path = r"C:\Users\chen\Downloads\takeout-20240822T141127Z-005\Takeout\YouTube ו-YouTube Music\סרטונים"

# Specify the expressions to filter filenames
expressions = ["דגגה"]  # Add more expressions as needed

# Define the CSV file path for output
csv_file_path = os.path.join(root_folder_path, "filtered_filenames.csv")

# Read the existing filenames from the CSV file
existing_filenames = read_existing_filenames(csv_file_path)

# Prepare to write to the CSV file
with open(csv_file_path, mode='a', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header if the file is empty
    if os.stat(csv_file_path).st_size == 0:
        writer.writerow(["Filename"])

    # Walk through each directory in the root folder
    for dirpath, dirnames, filenames in os.walk(root_folder_path):
        # Filter the filenames based on the expressions
        filtered_filenames = filter_filenames(filenames, expressions)

        # Append only new filtered filenames to the CSV file
        for filename in filtered_filenames:
            full_path = os.path.join(dirpath, filename)
            if full_path not in existing_filenames:
                writer.writerow([full_path])
                existing_filenames.add(full_path)

print(f"New filtered filenames appended to {csv_file_path}")
