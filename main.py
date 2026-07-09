from LoginMenu import log_register
from Employeedb import employeedb

def main():
    auth = log_register()
    db = employeedb()
    
    while True:
        print("\n" + "="*40)
        print("    EMPLOYEE MANAGEMENT SYSTEM")
        print("="*40)
        print("1. REGISTER")
        print("2. LOGIN")
        print("0. EXIT")
        print("="*40)
        
        try:
            choice = int(input("ENTER CHOICE 0-2: "))
            
            if choice == 1:
                auth.register()
                
            elif choice == 2:
                if auth.login():
                    employee_menu(db)
                    
            elif choice == 0:
                db.file_close()
                print("GOODBYE!")
                break
            else:
                print("ENTER BETWEEN 0-2")
                
        except ValueError:
            print("ENTER NUMBER")

def employee_menu(db):
    while True:
        print("\n" + "="*40)
        print("       EMPLOYEE MENU")
        print("="*40)
        print("1. ADD EMPLOYEE")
        print("2. VIEW EMPLOYEE")
        print("3. SEARCH EMPLOYEE")
        print("4. UPDATE EMPLOYEE")
        print("5. DELETE EMPLOYEE")
        print("6. COUNT EMPLOYEE")
        print("7. COUNT DEPARTMENT EMPLOYEE")
        print("8. AVERAGE SALARY")
        print("9. TOTAL SALARY")
        print("10. EXPORT CSV")
        print("0. LOGOUT")
        print("="*40)
        
        try:
            choice = int(input("ENTER CHOICE 0-10: "))
            
            if choice == 1:
                db.add_employee()
            elif choice == 2:
                db.view_employee()
            elif choice == 3:
                name = input("ENTER NAME TO SEARCH: ").strip()
                db.search_employee(name)
            elif choice == 4:
                db.update_menu()
            elif choice == 5:
                db.delete_employee()
            elif choice == 6:
                db.count_employee()
            elif choice == 7:
                db.count_department_employee()
            elif choice == 8:
                db.average_salary()
            elif choice == 9:
                db.TOTAL_salary()
            elif choice == 10:
                db.Export_csv()
            elif choice == 0:
                print("LOGGED OUT!")
                break
            else:
                print("ENTER BETWEEN 0-10")
                
        except ValueError:
            print("ENTER NUMBER")

main()