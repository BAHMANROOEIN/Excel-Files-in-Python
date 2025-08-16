import openpyxl
import os

os.system("cls")

load=openpyxl.load_workbook("test.xlsx")

sheet_sh=load["sh"]

names=["bahman" , "reza" , "ali"]

try:
    co=0
    for name in names :
        co=co+1
        sheet_sh.cell(column=co , row=1).value = name

    load.save("test.xlsx")
    print("Ok...")
    os.system("start test.xlsx")
except PermissionError :
    os.system("taskkill /im ""excel.exe")
    print("end...")