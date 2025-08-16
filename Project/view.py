import openpyxl , os

def view () :
    os.system("cls")
    load = openpyxl.load_workbook("contacts.xlsx")
    sheet_DB = load["DB"]
    for cell in sheet_DB :
        print(str(cell[0].value) + " | " + cell[1].value + " | " + str(cell[2].value ))
        print("===============================")
      


