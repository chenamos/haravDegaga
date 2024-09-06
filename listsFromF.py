import os
import csv

def list_files_recursively(root_path, extensions):
    """ Recursively lists all files in the given directory path with specific extensions. """
    file_details = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.split('.')[-1].lower() in extensions:
                file_details.append((os.path.splitext(file)[0], file))  # Store without extension and full name
    return file_details

def compare_files(path1, path2, extensions):
    """ Compares files between two directories based on the first 20 characters and records the results. """
    files_path1 = {name[:30]: full_name for name, full_name in list_files_recursively(path1, extensions)}
    files_path2 = {name[:30]: full_name for name, full_name in list_files_recursively(path2, extensions)}
    match_count = 0

    # Prepare data for CSV
    data_rows = []

    # Check each file in the first path
    for short_name1, full_name1 in files_path1.items():
        if short_name1 in files_path2:
            data_rows.append([full_name1, files_path2[short_name1], 'Yes'])
            match_count += 1
        else:
            data_rows.append([full_name1, '', 'No'])

    # Add files from the second path that are not in the first path
    for short_name2, full_name2 in files_path2.items():
        if short_name2 not in files_path1:
            data_rows.append(['', full_name2, 'No'])

    # Writing to CSV
    with open('file_comparison.csv', mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        # Write match count and header at the top
        writer.writerow(['Match Count', match_count])
        writer.writerow([f'Files in {path1}', f'Files in {path2}', 'Match'])

        # Write data rows
        writer.writerows(data_rows)

def main():
    path1 = r'F:\סרטונים'
    path2 = r'F:\הרב דגגה'
    extensions = ['mp4', 'avi']  # Only consider these extensions
    compare_files(path1, path2, extensions)

if __name__ == '__main__':
    main()
