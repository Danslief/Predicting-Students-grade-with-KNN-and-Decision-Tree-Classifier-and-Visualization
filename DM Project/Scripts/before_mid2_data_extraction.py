import pandas as pd

# Read the Excel file
excel_file = "D.xlsx"
xls = pd.ExcelFile(excel_file)

# Dictionary to store data frames for each   sheet
sheet_dict = {}

# Loop through each sheet and extract required columns
for sheet_name in xls.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    sheet_dict[sheet_name] = df[['As:1','As:2','As:3','As:4','Qz:1','As:2','As:3','Qz:4','S-I','Grade']]

# Write the extracted data to a new CSV file
output_csv = "model_train_before_mid2.csv"
with open(output_csv, 'w', newline='') as csvfile:
    for sheet_name, df in sheet_dict.items():
        df.to_csv(csvfile, mode='a', index=False, header=True)
