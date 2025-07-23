"""
    Renames all files in the specified folder.
"""
import os
directory_path = "/home/suser/Workspace/BookHub/bookhub/src/main/res/font"
old_char = "-"
new_char = "_"
try:
    for filename in os.listdir(directory_path):

        # Construct full path of the current file
        construct_full_path = os.path.join(directory_path, filename)
        
        # Check if it is a file not a directory
        if os.path.isfile(construct_full_path):
            # Create new file name with replaced characters
            # new_filename = filename.replace(old_char, new_char)
            new_filename = filename.lower()
            
            # Construct full path of the new file
            new_filename_path = os.path.join(directory_path, new_filename)
            
            # Rename the file
            os.rename(construct_full_path, new_filename_path)
            
            # Only rename if the case is different
            if old_file_path != new_file_path:
                try:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed '{filename}' to '{new_filename}'")
                except OSError as e:
                    print(f"Error renaming '{filename}': {e}")
except FileNotFoundError:
    print(f"Error: Directory not found at {directory_path}")
except PermissionError:
    print(f"Error: Permission denied to access files in {directory_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
