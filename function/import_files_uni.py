import glob
import json

# If needed, use global and non-relative path to solve 'glob' module issues
# import os
# path = 'C://Users/vince/Documents/Université/M1/Programming Basics/Python_Class_Cal_Counter-main/'
# os.chdir(path)

all_files = glob.glob("data/*.json")
all_files

names_files: list = []

for full_path in all_files:
    names_files.append(full_path[5:-5])

names_files

for y in range(0, len(all_files)):
    temp_dict: dict = {}
    file = open(str(all_files[y]))
    temp_dict = json.load(file)
    for key in temp_dict:
        (globals()[str(names_files[y])]): list = list(temp_dict[key])
