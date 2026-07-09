import sqlite3
import re
import csv
class employeedb:
    def __init__(self):
        self.con = sqlite3.connect('Employee.db')
        self.cusor=self.con.cursor()
        self.construct_table()
    def construct_table(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS employee(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            department TEXT,
            salary INTEGER,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE,
            joining_date TEXT
            )
        """)
        self.con.commit()
    def insert_value(self,name,age,department,salary,email,phone,joining_date):
        try:
            self.cusor.execute('''
                INSERT INTO employee(name,age,department,salary,email,phone,joining_date)
                VALUES(?,?,?,?,?,?,?)
            ''',(name,age,department,salary,email,phone,joining_date))
            self.con.commit()
        except sqlite3.IntegrityError:
            print("EMAIL OR PHONE NO ALREADY EXIST")
    def valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        self.cusor.execute("SELECT * FROM employee WHERE email = ?", (email,))
        user = self.cusor.fetchone()
        if user :
            print("EMAIL ALREADY EXIST")
            a= False
        else:
            a=True
        return re.fullmatch(pattern, email) is not None and a
    def valid_phone(self,phone):
        pattern = r"^0\d{10}$"
        self.cusor.execute("SELECT * FROM employee WHERE phone = ?",(phone,))
        user=self.cusor.fetchone()
        if user:
            print("PHONE NUMBER ALREADY EXIST")
            a=False
        else:
            a=True
        return re.fullmatch(pattern,phone) is not None and a
    def valid_date(self,joining_date):
        pattern=r"^\d{4}[-./]\d{2}[-./]\d{2}$"
        return re.fullmatch(pattern,joining_date) is not None
    def add_employee(self):
        self.name=input("ENTER YOUR NAME: ").strip()
        self.age=int(input("ENTER YOUR AGE: "))
        self.department=input("ENTER YOUR DEPARTMENT: ").strip()
        self.salary=int(input("ENTER YOUR SALARY: "))
        while True:
            self.email=input("ENTER YOUR EMAIL: ").strip().lower()
            if self.valid_email(self.email):
                break
            print("Enter Valid Email")
        while True:
            self.phone=input("ENTER YOUR PHONE NUMBER: ").strip()
            if self.valid_phone(self.phone):
                break
            print ("ENTER VALID PHONE NUMBER")
        while True:
            self.joining_date=input("ENTER JOINING DATE (2026-07-09): ").strip()
            if self.valid_date(self.joining_date):
                break
            print("ENTER CORRECT FORMAT OF DATE (YEAR-MONTH-DATE)")
        self.insert_value(self.name,self.age,self.department,self.salary,self.email,self.phone,self.joining_date)
    def view_employee(self):
        self.cusor.execute("SELECT * FROM employee")
        print(f"{'ID':<15}{'Name':<15}{'AGE':<5}{'Department':<15}{'Salary':<15}{'Email':<15}{'Phone':<15}{'Joining Date':<15}")
        print('='*97)
        for e in self.cusor.fetchall():
            print(f"{e[0]:<15}{e[1]:<15}{e[2]:<5}{e[3]:<15}{e[4]:<15}{e[5]:<15}{e[6]:<15}{e[7]:<15}")
    def search_employee(self,name):
        self.cusor.execute("SELECT * FROM employee WHERE name LIKE ?",(f'%{name}%',))
        print(f"{'Name':<15}{'Email':<15}{'Phone no':<15}{'Department':<15}")
        print('='*65)
        for e in self.cusor.fetchall():
            print(f"{e[1]:<15}{e[5]:<15}{e[6]:<15}{e[3]:<15}")
    def update_phone(self):
        self.name=input("ENTER NAME YOU WANT TO UPDATE PHONE NO: ").strip()
        while True:
            self.phone=input("ENTER NEW PHONE: ")
            if self.valid_phone(self.phone):
                break
            print("ENTER CORRECT PHONE NUMBER")
        self.cusor.execute("""UPDATE employee 
        Set phone = ?
        WHERE name = ?
        """,(self.phone,self.name))
        self.con.commit()
    def update_email(self):
        self.name=input("ENTER NAME YOU WANT TO UPDATE Email: ").strip()
        while True:
            self.email=input("ENTER NEW EMAIL: ")
            if self.valid_email(self.email):
                break
            print("ENTER CORRECT EMAIL")
        self.cusor.execute("""UPDATE employee 
        Set email = ?
        WHERE name = ?
        """,(self.email,self.name))
        self.con.commit()
    def update_joiningdate(self):
        self.name=input("ENTER NAME YOU WANT TO UPDATE Joining date: ").strip()
        while True:
            self.joining_date=input("ENTER NEW joining date: ")
            if self.valid_date(self.joining_date):
                break
            print("ENTER CORRECT DATE")
        self.cusor.execute("""UPDATE employee 
        Set joining_date = ?
        WHERE name = ?
        """,(self.joining_date,self.name))
        self.con.commit()
    def update_departmet(self):
        self.name=input("ENTER NAME YOU WANT TO UPDATE DEPARTMENT: ").strip()
        self.department=input("ENTER NEW DEPARTMENT: ")
        self.cusor.execute("""UPDATE employee 
        Set department = ?
        WHERE name = ?
        """,(self.department,self.name))
        self.con.commit()
    def update_salary(self):
        self.name=input("ENTER NAME YOU WANT TO UPDATE SALARY: ").strip()
        self.salary=input("ENTER NEW SALARY: ")
        self.cusor.execute("""UPDATE employee 
        Set salary = ?
        WHERE name = ?
        """,(self.salary,self.name))
        self.con.commit()
    def update_menu(self):
        while True:
            try:
                print("1.Update Phone")
                print("2.Update EMail")
                print("3.Update Joining date")
                print("4.Update Department")
                print("5.Update Salary")
                print("0.EXIT")
                choice=int(input("ENTER CHOICE 0-5: "))
                if choice == 1:
                    self.update_phone()
                elif choice==2:
                    self.update_email()
                elif choice==3:
                    self.update_joiningdate()
                elif choice==4:
                    self.update_departmet()
                elif choice==5:
                    self.update_salary()
                elif choice==0:
                    break
                else:
                    print("ENTER BETWEEN 0-5")
            except ValueError:
                print("ENTER NUMBER ")
    def delete_employee(self):
        self.name=input("ENTER YOUR NAME").strip()
        self.cusor.execute("DELETE FROM employee WHERE name = ?",(self.name,))
        self.con.commit()
    def count_employee(self):
        self.cusor.execute("SELECT COUNT(*) FROM employee")
        self.count = self.cusor.fetchone()[0]
        print(f"TOTAL EMPLOYEES: {self.count}")
    def count_department_employee(self):
        self.department=input("ENTER YOUR DEPARTMENT: ").strip()
        self.cusor.execute("SELECT COUNT(*) FROM employee WHERE department = ?",(self.department,))
        self.count = self.cusor.fetchone()[0]
        print(f"TOTAL EMPLOYEES: {self.count}")
    def average_salary(self):
        self.cusor.execute("SELECT * FROM employee")
        self.sum = 0          
        self.count = 0        
        for s in self.cusor.fetchall():
            self.sum += s[4]  
            self.count += 1   
        if self.count > 0:   
            self.avgsalary = self.sum / self.count
            print(f"AVERAGE SALARY: {self.avgsalary}")
        else:
            print("NO EMPLOYEE FOUND")
    def TOTAL_salary(self):
        self.cusor.execute("SELECT * FROM employee")
        self.sum = 0               
        for s in self.cusor.fetchall():
            self.sum += s[4]  
        print(f"TOTAL SALARY {self.sum}")
    def Export_csv(self,filename="Employee.csv"):
        self.cusor.execute("SELECT * FROM employee")
        employee = self.cusor.fetchall()
        if not employee:
            print ("NO EMPLOYEE")
            return
        with open(filename,'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID","Name","Age","Department","Salary","Email","Phone No","Joining date"])
            writer.writerows(employee)
            print(f"✅ Export done → {filename}")
    def file_close(self):
        self.con.close()
        print("File CLosed")
