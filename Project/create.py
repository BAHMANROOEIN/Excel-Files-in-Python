import openpyxl
import os

os.system("cls")

def create_ex (name_ex , name_sh) :
    name_ex = name_ex + ".xlsx"
    list = os.listdir()
    t_f=name_ex in list
    if t_f == True :
        pass
    else:
        new = openpyxl.Workbook()
        new.active.title = name_sh
        new.save(name_ex)
        load = openpyxl.load_workbook(name_ex)
        sheet = load[name_sh]
        sheet["A1"] = "ID"
        sheet["B1"] = "Names"
        sheet["C1"] = "Numbers"
        load.save(name_ex)
    return name_ex
