from create import create_ex
import openpyxl
import os
import time

name_ex = input("Please Enter Name excel : ")
name_sh = input("Please Enter Name Sheet : ")

create = create_ex(name_ex , name_sh)

time.sleep(2)

os.system("cls")

load=openpyxl.load_workbook(create)
sheet=load[name_sh]
sheet["A1"] = "Hi"
load.save(create)
print("Ok...")
os.system("start "+create)