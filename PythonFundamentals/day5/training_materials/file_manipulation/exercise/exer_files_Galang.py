import json
import os
import shutil
from pathlib import Path
import glob
import re

"""
    Use this file as a starting point for your exercise on File Manipulation
"""

CONFIG_PATH = "config.json"
COUNTRIES_FOLDER_NAME = "countries"
CONTINENTS_FOLDER_NAME = "continents"


def create_new_files():
    """
    A function that does the ff:
       1. Creates a new folder named after the COUNTRIES_FOLDER_NAME variable
       2. Reads the CONFIG_PATH file and creates an empty TEXT file for each
          'country' in that file
       3. Saves each file to COUNTRIES_FOLDER_NAME with the file name
          <name>_<continent>.txt
    """

    # HINT: You can combine path components (strings) into a single path
    #       by using os.path.join()

    os.makedirs(COUNTRIES_FOLDER_NAME, exist_ok=True)
    with open(CONFIG_PATH, "r") as country:
        content = json.load(country)

    country_list = content["countries"]

    for country in country_list:
        country_name = country["name"]
        country_continent = country["continent"]

        file_name = f"{'_'.join([country_name, country_continent])}.txt"
        file_path = os.path.join(os.getcwd(), COUNTRIES_FOLDER_NAME, file_name)

        with open(file_path, "w"):
            print(f"{file_name} created")


def find_files_by_continent(cont):
    """
    A function that searches for all files inside the COUNTRIES_FOLDER_NAME folder
    that has the input continent in its file name and returns a list of those file paths
    """
    current_path = os.getcwd()

    # /* only gets files that are in folders of current directory
    # outputs a list with "countries/<filename>.txt" format
    list_with_cont = [
        name for name in glob.glob("countries/*") if cont in name
    ]
    list_files = []

    # filters list_with_cont list so only filename is included in string
    for country in list_with_cont:
        match = re.sub(f"{COUNTRIES_FOLDER_NAME}(\/|\\\\)+", "", country)
        list_files.append(match)

    return list_files


def sort_files_by_continent():
    """
    A function that does the ff:
        1. Creates a directory called CONTINENTS_FOLDER_NAME and a subdirectory
           inside it for each unique continent in CONFIG_PATH
        2. Creates a copy of each file in COUNTRIES_FOLDER_NAME and saves it to its
           corresponding subdirectory CONTINENTS_FOLDER_NAME
    """
    os.makedirs(CONTINENTS_FOLDER_NAME, exist_ok=True)
    with open(CONFIG_PATH, "r") as country:
        content = json.load(country)

    country_list = content["countries"]
    continent_list = [i["continent"] for i in country_list]

    continent_set = set(continent_list)

    country_dir = os.path.join(os.getcwd(), COUNTRIES_FOLDER_NAME)

    for continent in continent_set:
        dir_path = os.path.join(os.getcwd(), CONTINENTS_FOLDER_NAME, continent)
        os.makedirs(dir_path, exist_ok=True)

        for file in find_files_by_continent(continent):
            file_path = os.path.join(country_dir, file)
            try:
                shutil.copy(file_path, dir_path)
                print(f"{file} copied to {continent} folder")
            except Exception as e:
                print(e)


def cleanup():
    """
    Deletes all the files and folders that were created
    """
    country_dir = os.path.join(os.getcwd(), COUNTRIES_FOLDER_NAME) 
    continent_dir = os.path.join(os.getcwd(), CONTINENTS_FOLDER_NAME) 
    
    try:
        shutil.rmtree(country_dir)
        shutil.rmtree(continent_dir)
    except OSError as e:
        print(f"Error: {e.strerror}")

