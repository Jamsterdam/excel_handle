# this is the main scrip body

import pandas as pd


# read the csv file, but I need to read it no matter what nane it has,
# for example, pd.read_csv('*.csv')
notion = pd.read_csv('Autol CRM a376400f34a2458797bd2abba4fd49e7.csv')


# read the related oem column
# process each row with the text_handle.py, and get replace the original cell of the spreadsheet
# export as xlsx file
