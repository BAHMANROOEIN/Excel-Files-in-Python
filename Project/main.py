import openpyxl , os , c_contact , view , edit , delete

os.system("cls")

print("======================================")
print("Welcome Back To Contact App")
print("======================================")

print("1 : Create Contact")
print("2 : View Contacts")
print("3 : Edit Contacts")
print("4 : Delete Contacts")
print("======================================")

try:
    inp_user = int(input("Please Enter Number (1-4) : "))
    if inp_user == 1 :
        c_contact.c_contact()
    elif inp_user == 2 :
        view.view()
    elif inp_user == 3 :
        edit.edit()
    elif inp_user == 4 :
        delete.delete()
    else :
        os.system("cls")
        print("Please Enter Number (1-4)...!")
except ValueError :
    os.system("cls")
    print("Please Enter Number...!")