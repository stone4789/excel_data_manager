#! /usr/bin/env python3
def excelManager():
    import glob
    import numpy as np
    import openpyxl
    import os
    import pandas as pd
    import warnings

    warnings.filterwarnings("ignore")

    os.chdir(#"insert folder path here")
    # Double-check you're in the right folder
    path = os.getcwd()
    print(path)

    # Find all the CSVs. If they're xlsx, change the last argument
    excel_files = glob.glob(os.path.join(path, "*.csv"))

    # List of columns to use. All others will be ignored.
    cols_to_use = []

    # Lists for storing the names of the respective files
    mks_prodhd = []
    mks = []
    am_schd = []
    for file in all_excel_files:
        filename = os.fsdecode(file)
        if 'PRODHD' in filename:
            mks_prodhd.append(filename)
        elif 'Segment' in filename:
            mks.append(filename)
        else:
            am_schd.append(filename)