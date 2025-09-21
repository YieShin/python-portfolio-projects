import os
import shutil

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"],
}

def organize_files(folder_path):
    """Organizes files in the given folder by type."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        moved = False

        # Check which category the file belongs to
        for category, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved: {filename} → {category}/")
                moved = True
                break

        # If no match, move to "Others"
        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} → Others/")

if __name__ == "__main__":
    target_folder = os.getcwd()  # Default: current folder
    print(f"Organizing files in: {target_folder}")
    organize_files(target_folder)
    print("✅ Done organizing!")