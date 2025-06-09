# %%

import os
import shutil
import datetime
import pandas as pd

def frisatday():

    # Creating paths for each step of expenses extraction

    source_path = "C:\\Users\\pavel\\OneDrive\\Desktop\\My_projects\\Expenses_extraction\\expext\\SourcePath"
    process_path = "C:\\Users\\pavel\\OneDrive\\Desktop\\My_projects\\Expenses_extraction\\expext\\ProcessPath"
    done_path = "C:\\Users\\pavel\\OneDrive\\Desktop\\My_projects\\Expenses_extraction\\expext\\DonePath"

    # Getting the csv files names from the "SourcePath" directory

    data_source = os.listdir(source_path)
    data_source_related = []
    for file in data_source:
        if ".csv" in file:
            data_source_related.append(file)
    print(data_source_related)

    


if __name__ == "__main__":
    # Tests

    # Creating paths for each step of expenses extraction

    source_path = "C:\\Users\\pavel\\OneDrive\\Desktop\\My_projects\\Expenses_extraction\\expext\\SourcePath"
    process_path = "C:\\Users\\pavel\\OneDrive\\Desktop\\My_projects\\Expenses_extraction\\expext\\ProcessPath"
    done_path = "C:\\Users\\pavel\\OneDrive\\Desktop\\My_projects\\Expenses_extraction\\expext\\DonePath"

    # Getting the csv files names from the "SourcePath" directory

    data_source = os.listdir(source_path)
    data_source_related = []
    for file in data_source:
        if ".csv" in file:
            data_source_related.append(file)
    print(data_source_related)

# %%
