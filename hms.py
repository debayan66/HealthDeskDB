import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',password='qwerty',database='assign1',auth_plugin='mysql_native_password')
cur = con.cursor()
from tabulate import tabulate

def execute():
    yn = input("Confirm? (y/n) ")
    if yn == "y":
        con.commit()
        print("Done.")

def entry():
    def doc():
        DID = input("Enter Doctor ID: ")
        name = input("Enter name: ")
        p = int(input("Enter phone number: "))
        spc = input("Enter specialization: ")
        qry = "INSERT INTO DOCTORS VALUES(%s, %s, %s, %s, %s);"
        t1 = (DID, name, p, spc)
        cur.execute(qry, t1)
        execute()

    def adm():
        # Calculating PID from table
        cur.execute("SELECT PATIENTID FROM ADMISSION;")
        r = cur.fetchall()
        lastP = r[-1][0]
        l = lastP.split("P")
        l[-1] = int(l[-1]) + 1
        f = len(l)
        PID = "P"
        for x in range(f, 3):
            PID += "0"
        PID += str(l[-1])

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        s = input("Enter sex: ")
        DoA = input("Enter date of admission: ")

        # BED number once allotted cannot be used again. It can be used only when the patient is discharged
        # i.e., DOD (date of discharge) is filled.
        bed = input("Enter bed number: ")
        cur.execute("SELECT BED, DOD FROM ADMISSION;")
        rows1 = cur.fetchall()
        for i in rows1:
            if bed in rows1[i]:
                for j in range(len(rows1[i])):
                    dod = rows1[i][j]
                    while dod == None:
                        print("Bed currently in use.")
                        bed = input("Enter bed number: ")

        adB = input("Enter admitted by: ")
        relt = input("Enter relation: ")
        p = int(input("Enter phone number: "))
        diagn = input("Enter diagnosis: ")

        # Discharge confirmation
        yn = input("Is the patient discharged? (y/n) ")
        if yn == "y":
            DoD = input("Enter date of discharge: ")

        # Attending Doctor must be present in the doctor's table
        cur.execute("SELECT NAME FROM DOCTORS;")
        rows2 = cur.fetchall()
        for i in rows2:
            attDoc = input("Enter attending doctor's name: ")
            while attDoc not in rows2[i]:
                print("Invalid Doctor name")
                attDoc = input("Enter attending doctor's name: ")

        qry = "INSERT INTO ADMISSION VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        t2 = (PID, name, age, s, DoA, bed, adB, relt, p, diagn, DoD, attDoc)
        cur.execute(qry, t2)
        execute()

    def chrg():
        cur.execute("SELECT PATIENTID FROM ADMISSION;")
        rows = cur.fetchall()
        PID = input("Enter Patient ID: ")
        for i in rows:
            while PID != rows[i]:
                print("Patient ID does not exist.")
                PID = input("Enter Patiend ID: ")

        DoT = input("Enter Date of Transaction: ")
        prtclr = int(input("Enter Particulars: "))
        amt = int(input("Enter Amount: "))

        qry = "INSERT INTO MARKS VALUES(%s, %s, %s, %s, %s)"
        t3 = (PID, DoT, prtclr, amt)
        cur.execute(qry, t3)
        execute()

    def bill():
        cur.execute("SELECT PATIENTID FROM ADMISSION;")
        rows = cur.fetchall()
        PID = input("Enter Patient ID: ")
        for i in rows:
            while PID != rows[i]:
                print("Patient ID does not exist.")
                PID = input("Enter Patiend ID: ")

        DoB = input("Enter Date Of Billing: ")
        amt = int(input("Enter Amount: "))

        qry = "INSERT INTO MARKS VALUES(%s, %s, %s)"
        t1 = (PID, DoB, amt)
        cur.execute(qry, t1)
        execute()

    while True:
        c = int(input("1) Add new doctors \n2) New Admissions \n3) Daily Charges \n4) Bill Collection \n Enter your choice: "))
        if c == 1:
            doc()
            break
        elif c == 2:
            adm()
            break
        elif c == 3:
            chrg()
            break
        elif c == 4:
            bill()
            break
        else:
            print("Invalid Choice. Please enter a number between 1 and 4.")
            c = int(input("Enter your choice: "))

def reports():
    print("*" * 10)
    print("REPORTS")
    print("*" * 10)
    print("Menu: \n")
    print("1) List of doctors")
    print("2) Search doctors by name")
    print("3) Search doctors by specialization")
    print("4) Search patients admitted on a particular day")
    print("5) Search admitted patients by name")
    print("6) Search admitted patients by gender")
    print("7) Search admitted patients by attending doctor")
    print("8) Search admitted patients by diagnosis")
    print("9) Detail treatment and expenses of a particular patient")
    print("10) List of patients discharged on a particular day")
    print("11) Total collection in a data range")
    print("*" * 10)

    c = int(input("Enter your choice from above menu: "))
    print("*" * 10)
    try:
        if c == 1:
            cur.execute("SELECT * FROM DOCTORS;")
            row = cur.fetchall()
            print(tabulate(row, headers=list(row[0]), tablefmt="rounded_outline"))

        elif c == 2:
            nm = input("Enter required doctor name: ")
            cur.execute(f"SELECT * FROM DOCTORS WHERE NAME='{nm}';")
            row = cur.fetchall()
            print(tabulate(row, headers=list(row[0]), tablefmt="rounded_outline"))

        elif c == 3:
            sp = input("Enter required specialization: ")
            cur.execute(f"SELECT * FROM DOCTORS WHERE SPECIALIZATION='{sp}';")
            row = cur.fetchall()
            print(tabulate(row, headers=list(row[0]), tablefmt="rounded_outline"))

        elif c == 4:
            da = input("Enter required date (YYYY-DD-MM): ")
            cur.execute(f"SELECT * FROM ADMISSION WHERE DoA='{da}';")
            row = cur.fetchall()
            print(tabulate(row, headers=list(row[0]), tablefmt="rounded_outline"))

        elif c == 5:
            pnm = input("Enter required patient name: ")
            cur.execute(f"SELECT * FROM ADMISSION WHERE NAME='{pnm}';")
            row = cur.fetchall()
            print(tabulate(row, headers=list(row[0]), tablefmt="rounded_outline"))

        elif c == 6:
            dnm = input("Enter required doctor name: ")
            cur.execute(f"SELECT * FROM DOCTORS WHERE NAME={dnm};")
            row = cur.fetchall()
            print(tabulate(row, headers=list(row[0]), tablefmt="rounded_outline"))

        elif c == 7:
            ge = input("Enter required gender: ")
            cur.execute(f"SELECT * FROM ADMISSION WHERE GENDER={ge};")
            row = cur.fetchall()
            print(tabulate(row, headers=list(row[0]), tablefmt="rounded_outline"))

        elif c == 8:
            nm = input("Enter required diagnosis: ")
            cur.execute(f"SELECT * FROM ADMISSION WHERE DIAGN='{nm}';")
            row = cur.fetchall()
            print(tabulate(row, headers=list(row[0]), tablefmt="rounded_outline"))

        elif c == 9:
            PID = input("Enter Patient ID: ")
            cur.execute(f"SELECT * FROM DAILYCHARGES WHERE PATIENTID = {PID};")
            row = cur.fetchall()
            print(tabulate(row, headers=list(row[0]), tablefmt="rounded_outline"))

        elif c == 10:
            date = input("Enter date (YYYY-MM-DD): ")
            cur.execute(f"SELECT * FROM ADMISSION WHERE DOD = '{date};")
            row = cur.fetchall()
            print(tabulate(row, headers=list(row[0]), tablefmt="rounded_outline"))

        elif c == 11:
           d1 = input("Enter start date (YYYY-MM-DD):")
           d2 = input("Enter end date (YYYY-MM-DD): ")
           cur.execute(f"SELECT AMOUNT FROM DAILYCHARGES WHERE DOT >= '{d1}' AND DOT <= '{d2}');")

        else:
            raise ValueError("Invalid Choice")
    except ValueError as e:
        print(e)
        c = int(input("Please enter a valid choice: "))

def tools():
    print("1) Delete unwanted admission entry \n2) Delete unwanted daily charges entry")
    c = int(input("Enter your choice from above menu: "))
    e = input("Enter Patient ID to delete their record: ")

    if c == 1:
        cur.execute(f"DELETE FROM ADMISSION WHERE PATENTID ='{e}';")
        execute()
    elif c == 2:
        cur.execute(f"DELETE FROM DAILYCHARGES WHERE PATIENTID ='{e}';")
        execute()

def ext():
    x = input("Exit the application? (y/n): ")
    if x == "y":
        exit()

print("1) Entry \n2) Reports \n3) Tools \n4) Exit")
menu = int(input("Enter your choice from above menu: "))
try:
    if menu == 1:
        entry()
    elif menu == 2:
        reports()
    elif menu == 3:
        tools()
    elif menu == 4:
        ext()
    else:
        raise ValueError("Invalid Choice")
except ValueError as e:
    print(e)
    menu = int(input("Please enter a valid choice: "))
