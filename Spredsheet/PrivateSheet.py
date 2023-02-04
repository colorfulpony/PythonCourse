import gspread

gc = gspread.service_account('secrets.json')

spreadsheet = gc.open('Copy of Accountant - Florida ')

worksheet1 = spreadsheet.worksheet('HUB_20230127_(3781)')

#get a rows
row = worksheet1.get_values('A5:E5')

#get a column
column = worksheet1.get_values('A5:A25')



#UPDATE CELL
worksheet1.update('D3', 'Voip')



#UPDATE COLUMNS
existing_column = worksheet1.get_values("E2:E25")
new_column = [float(i[0]) for i in existing_column]
print(new_column)