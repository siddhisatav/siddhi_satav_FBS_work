import os

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def record(self):
        return f"{self.eid}|{self.ename}|{self.basic}\n"


FILE = "emp.txt"


def add_record():
    eid = input("Enter Emp ID: ")
    ename = input("Enter Name: ")
    basic = input("Enter Basic Salary: ")

    e = Emp(eid, ename, basic)

    with open(FILE, "a") as f:
        f.write(e.record())

    print("Record added successfully")


def search_record():
    eid = input("Enter Emp ID to search: ")
    found = False

    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == eid:
                print("Record Found")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Basic:", data[2])
                found = True
                break

    if not found:
        print("Record not found")


def delete_record():
    eid = input("Enter Emp ID to delete: ")
    found = False

    with open(FILE, "r") as f:
        lines = f.readlines()

    with open(FILE, "w") as f:
        for line in lines:
            data = line.strip().split("|")
            if data[0] != eid:
                f.write(line)
            else:
                found = True

    if found:
        print("Record deleted")
    else:
        print("Record not found")


def edit_record():
    eid = input("Enter Emp ID to edit: ")
    found = False

    with open(FILE, "r") as f:
        lines = f.readlines()

    with open(FILE, "w") as f:
        for line in lines:
            data = line.strip().split("|")
            if data[0] == eid:
                ename = input("Enter New Name: ")
                basic = input("Enter New Basic Salary: ")
                e = Emp(eid, ename, basic)
                f.write(e.record())
                found = True
            else:
                f.write(line)

    if found:
        print("Record updated")
    else:
        print("Record not found")


def display_all():
    if not os.path.exists(FILE):
        print("No records available")
        return

    with open(FILE, "r") as f:
        records = f.readlines()

    if not records:
        print("No records found")
        return

    print("\nEmpID  Name   Basic")
    print("-" * 25)
    for line in records:
        data = line.strip().split("|")
        print(data[0], data[1], data[2])


# -------- MENU --------
while True:
    print("\n1.Add Record")
    print("2.Search Record")
    print("3.Delete Record")
    print("4.Edit Record")
    print("5.Display All")
    print("6.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_record()
    elif ch == "2":
        search_record()
    elif ch == "3":
        delete_record()
    elif ch == "4":
        edit_record()
    elif ch == "5":
        display_all()
    elif ch == "6":
        break
    else:
        print("Invalid choice")
