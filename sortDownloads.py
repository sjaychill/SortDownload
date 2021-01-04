import os
from pathlib import Path
# Dictionary that contains folder name and extension for each
# folder for the sorting.
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt', '.docx'],
    "MUSIC": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4', '.mkv'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}
# checking if the suffix or extension is in the subdirectory


def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'


# function to organize the files in your directory
def organizeDirectory():
    # use scandir function from "os" libary to check all the directory
    # and get all the folders

    for items in os.scandir():
        if items.is_dir():
            continue
        # use the Path function from "pathlib" to get the filepath
        filePath = Path(items)
        # issolate the suffix(file extension)  and determine the directory it should go into
        # then stored in a variable called filetype
        filetype = filePath.suffix.lower()
        # now we call our pickDirectory function and pass filetype as arguement
        # store it in a variable called directory
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        # decision : if directory doesn't exist  create a new directory
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))


organizeDirectory()
