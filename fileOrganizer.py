# Python program that automatically organizes any folder using Python

# Imports
from os import listdir
from os.path import isfile, join
import os
import shutil


# Gets a file path from the user
file_path = str(input("Please input the address of the directory you'd like to organize:"))

# Gets files from the path and stores them in a list
files = [file for file in listdir(file_path) if isfile(join(file_path, file))]

# Create the blank list and dictionary
file_type_list = []
file_type_dictionary = {}

# Loops through files in inputted folder and separates file type from file
# Creates new folder for file type if a folder for the file type does not exist
for file in files:

    # Splits the file type from the file name by the last period (accounts for periods in file names)
    _, _, file_type = file.rpartition('.')

    # Check if the file type is in the list of file types
    if file_type not in file_type_list:

        # Adds the file type to the list of file types if it isn't in it already
        file_type_list.append(file_type)

        # Names the new folder for a specific type of file
        new_folder_name = file_path + '/' + file_type.upper() + ' Files'

        # Add the new folder name to the file type dictionary with key value pairs (Ex: pdf : PDF Files)
        file_type_dictionary[str(file_type)] = str(new_folder_name)

        # Check if the folder for a specific type of file exists
        if os.path.isdir(new_folder_name):

            # Exits the loop if the folder exists
            continue
        else:

            # Create the new folder if it does not exist
            os.mkdir(new_folder_name)

# Declare a index variable with value 1 to use for denoting the order of file movements
i = 1

# Loops through files in inputted folder
for file in files:

    # Gets the source path of each file
    source_path = file_path + '/' + file

    # Splits the file type from the file name by the last period (accounts for periods in file names)
    _, _, filetype = file.rpartition('.')

    # Checks if the file type exists in the file type dictionary
    if filetype in file_type_dictionary.keys():
        # Add the file type in dictionary if not already there
        destination_path = file_type_dictionary[str(filetype)]

        # Move the file from the original location to the newly created folder
        shutil.move(source_path, destination_path)

    # Prints where a file is being moved from and to
    print(i, '. ', source_path + ' >>> ' + destination_path)

    # Increment the value of index variable by 1
    i = i + 1
