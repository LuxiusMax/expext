# %%

import os
import shutil
from datetime import datetime
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
            shutil.move(f"{source_path}\\{data_source_related[0]}", f"{process_path}\\{data_source_related[0]}")
            df = pd.read_csv(f"{process_path}\\{data_source_related[0]}")
            print(df)



    


if __name__ == "__main__":
    # Tests

    # Creating paths for each phase of file processing

    source_path = "C:\\Users\\pavel\\OneDrive\\Desktop\\My_projects\\Expenses_extraction\\expext\\SourcePath"
    process_path = "C:\\Users\\pavel\\OneDrive\\Desktop\\My_projects\\Expenses_extraction\\expext\\ProcessPath"
    done_path = "C:\\Users\\pavel\\OneDrive\\Desktop\\My_projects\\Expenses_extraction\\expext\\DonePath"

    # creating an empty dataframs

    df_total = pd.DataFrame()

    data_source = os.listdir(source_path)
    data_source_related = [f for f in data_source if f.endswith(".csv")]
    for file in data_source_related:
        shutil.move(f"{source_path}\\{file}", f"{process_path}\\{file}")         
        df_temp = pd.read_csv(f"{process_path}\\{file}", encoding = "utf-8")
        df_temp.dropna(axis = 0, how = 'any', inplace= True, ignore_index= True)
        df_temp.columns = df_temp.loc[0]
        df_temp.drop(index = 0, inplace= True)
        print(df_temp)
        print(df_temp.columns)
        print(file)
        df_temp["מספר רכב"] = df_temp["car_number"]
        print(df_temp)
    
    for file in data_source_related:
        shutil.move(f"{process_path}\\{file}", f"{source_path}\\{file}")
    print(os.listdir(source_path))


# %%




# %%
