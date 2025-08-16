import openpyxl
import os

os.system("cls")

load=openpyxl.load_workbook("test.xlsx")

sheet_sh=load["sh"]

#a=sheet_sh["A2"].value

#for cell in sheet_sh :

    #print(cell[0].value)

#sheet_sh["A2"] = " "

#load.save("test.xlsx")

#print("ok...")

#sheet_sh.delete_rows(2)
#sheet_sh.delete_cols(2)



