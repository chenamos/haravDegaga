import os
import csv

def list_files_recursively(path, total_files, from_takeout):
    # Define a set of allowed extensions, normalized to lower case for case-insensitive comparison
    allowed_extensions = {'.mp3', '.mp4', '.avi', '.mts', 'wav'}

    for entry in os.scandir(path):
        if entry.is_dir():
            list_files_recursively(entry.path, total_files, from_takeout)  # Recursive call
        else:
            filename = os.path.basename(entry.path)  # Extract just the filename
            extension = os.path.splitext(filename)[1].lower()  # Extract and normalize the file extension

            if extension in allowed_extensions:
                if 'Takeout' in entry.path:
                    from_takeout.append(filename)  # Add filename to the Takeout list if in allowed extensions
                else:
                    total_files.append(filename)  # Add filename to the Total Files list if in allowed extensions

def write_to_csv(file_path, total_files, from_takeout):
    with open(file_path, mode='w', newline='', encoding='utf-8-sig') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Total Files', 'From Takeout'])  # Header row
        max_length = max(len(total_files), len(from_takeout))
        for i in range(max_length):
            row = [
                total_files[i] if i < len(total_files) else '',
                from_takeout[i] if i < len(from_takeout) else ''
            ]
            csv_writer.writerow(row)

# Specify the root paths for recursive processing
path1 = r'F:\הרב דגגה'
path2 = r'C:\Users\chen\Downloads\takeout-20240822T141127Z-005\Takeout\YouTube ו-YouTube Music\סרטונים'

# Lists to store filenames
total_files = []
from_takeout = []

# Process each path recursively
list_files_recursively(path1, total_files, from_takeout)
list_files_recursively(path2, total_files, from_takeout)

# Write the results to a CSV file in the specified directory
csv_file_path = r'F:\הרב דגגה\filenames.csv'
write_to_csv(csv_file_path, total_files, from_takeout)

print("CSV file has been written successfully with filenames.")
