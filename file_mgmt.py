import os
import shutil
from typing import List

def get_folder_paths(directory: str) -> list:
    """
    Gets list of folder in a given directory
    """
    folder_paths = []
    for root, dirs, files in os.walk(directory):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            folder_paths.append(folder_path)
    return folder_paths



def detect_mp4_files(directory):
    mp4_files = []
    for file in os.listdir(directory):
        if file.endswith(".mp4"):
            file_path = os.path.join(directory, file)
            mp4_files.append(file_path)
    return mp4_files


def move_file(source_file: str, destination_folder: str) -> None:
    """
    Move a file from the source file path to the destination folder.

    Args:
        source_file (str): The path to the source file.
        destination_folder (str): The path to the destination folder.

    Returns:
        None: The function does not return anything.

    Raises:
        FileNotFoundError: If the source file does not exist.
        IsADirectoryError: If the source file is a directory.
        shutil.Error: If an error occurs while moving the file.
    """
    if not os.path.exists(source_file):
        raise FileNotFoundError("Source file does not exist.")
    if not os.path.isfile(source_file):
        raise IsADirectoryError("Source file is a directory.")
    
    # Extract the file name from the source file path
    file_name = os.path.basename(source_file)
    # Create the destination path by combining the destination folder with the file name
    destination_path = os.path.join(destination_folder, file_name)
    # Move the file to the destination folder
    shutil.move(source_file, destination_path)
    print(f"File {file_name} moved successfully to {destination_path}")



import os
from typing import List

def remove_mp4_extension(folder_names: List[str]) -> None:
    """
    Remove the '.mp4' extension from the folder names and rename the folders.

    Args:
        folder_names (List[str]): A list of folder names.

    Returns:
        None: The function does not return anything.

    Raises:
        FileNotFoundError: If a folder with the specified name does not exist.
        NotADirectoryError: If a folder name points to a file instead of a directory.

    Examples:
        >>> folder_names = ["folder1.mp4", "folder2.mp4", "folder3"]
        >>> remove_mp4_extension(folder_names)
        Renamed folder: folder1.mp4 to folder1
        Renamed folder: folder2.mp4 to folder2
    """
    for folder_name in folder_names:
        if folder_name.endswith(".mp4"):
            new_name = folder_name[:-4]
            old_path = os.path.join(os.getcwd(), folder_name)
            new_path = os.path.join(os.getcwd(), new_name)
            os.rename(old_path, new_path)
            print(f"Renamed folder: {folder_name} to {new_name}")



########################################################################################

# Specify the directory path
destination_tracks_path = '/home/nesov/Programmation/youtube_dl/Tracks'

# Get the list of folder paths
folder_paths = get_folder_paths(destination_tracks_path)
remove_mp4_extension(folder_paths)
folder_paths = get_folder_paths(destination_tracks_path) # again because no .mp4 anymore

# Print the folder paths
for path in folder_paths:
    mp4_files = detect_mp4_files(path)
    for mp4_path in mp4_files:
        move_file(mp4_path, destination_tracks_path)