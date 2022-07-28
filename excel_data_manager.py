#! /usr/bin/env python3
def excelManager():
    import glob
    import numpy as np
    import openpyxl
    import os
    import pandas as pd
    import warnings

    warnings.filterwarnings("ignore")
    # Insert folder path here
    os.chdir("")
    # Double-check you"re in the right folder
    path = os.getcwd()
    print(path)

    # Find all the CSVs. If they"re xlsx, change the last argument
    excel_files = glob.glob(os.path.join(path, "*.csv"))

    # List of columns to use. All others will be ignored.
    cols_to_use = []

    # Lists for storing the names of the respective files
    mks_prodhd = []
    mks = []
    am_schd = []
    for file in excel_files:
        filename = os.fsdecode(file)
        if "PRODHD" in filename:
            mks_prodhd.append(filename)
        elif "Segment" in filename:
            mks.append(filename)
        else:
            am_schd.append(filename)

    def category_cleaner(category_list: list):
        for file in category_list:
            # Ignore "hidden" files
            if "$" not in file:
                temp_df = pd.read_csv(file, usecols=cols_to_use)
                temp_df.rename(
                    columns={
                        "Proprietary data removed here, use whatever new column names you want in a new dictionary"
                    }
                new_df = pd.concat([new_df, temp_df], ignore_index=True, sort=False)
                final_spreadsheet = final_spreadsheet.drop_duplicates()
                final_spreadsheet["ID"] = final_spreadsheet["ID"].astype("str") + "-" + final_spreadsheet["Warehouse"].astype("str")
                ids = final_spreadsheet["ID"].unique()
                to_keep = []
                for id in ids:
                    id_df = final_spreadsheet.loc[final_spreadsheet["ID"] == id]
                    if id_df["Quantity"].count() > 24:
                        to_keep.append(id)
                final_spreadsheet = final_spreadsheet[final_spreadsheet["ID"].isin(to_keep)]
        return final_spreadsheet
                )
