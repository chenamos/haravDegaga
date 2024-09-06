import os

def rename_files(root_path):
    """ Recursively renames files to remove underscores in the filenames within the given directory path. """
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if '_' in file:
                new_file_name = file.replace('_', '')
                original_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, new_file_name)
                os.rename(original_file_path, new_file_path)
                print(f"Renamed '{file}' to '{new_file_name}'")

def main():
    path1 = r'F:\סרטונים'
    rename_files(path1)

if __name__ == '__main__':
    main()
