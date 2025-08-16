import openpyxl
import os

os.system("cls")

def create_ex (name_ex , name_sh) :
    name_ex = name_ex + ".xlsx"
    list = os.listdir()
    t_f=name_ex in list
    if t_f == True :
        print("Find....")
    else:
        new = openpyxl.Workbook()
        new.active.title = name_sh
        new.save(name_ex)
        print("Create...!")
    return name_ex
