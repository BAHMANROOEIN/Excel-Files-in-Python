import openpyxl , os

os.system("cls")

load = openpyxl.load_workbook("test.xlsx")

sheet_sh = load["sh"]

sheet_sh.insert_rows(4)

sheet_sh.insert_cols(2)

load.save("test.xlsx")
print("ok...")
os.system("start test.xlsx")