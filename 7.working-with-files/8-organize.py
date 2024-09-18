import os
import shutil

# Define file categories and their corresponding extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.md'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Others': []  # Files that do not match any of the above categories
}

def organize_files_on_desktop():
    # Get the path to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Create directories for each category if they don't exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(desktop_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Iterate over all files on the desktop
    for item in os.listdir(desktop_path):
        original_item_path = os.path.join(desktop_path, item)
        
        # Skip directories
        if os.path.isdir(original_item_path):
            continue
        
        # Get the file extension
        _, file_extension = os.path.splitext(item)
        
        # Determine the category for the file
        file_category = 'Others'
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                file_category = category
                break
        
        # Move the file to the appropriate category directory
        if file_category != 'Others':
            destination_dir = os.path.join(desktop_path, file_category)
            shutil.move(original_item_path, os.path.join(destination_dir, item))
        else:
            # Optionally, handle files that don't match any category
            print(f"File '{item}' does not match any defined category.")

if __name__ == "__main__":
    organize_files_on_desktop()
