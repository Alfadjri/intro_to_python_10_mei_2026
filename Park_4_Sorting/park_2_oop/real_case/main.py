from data_kariwan.Manager import Manager
from data_kariwan.Employee import Employee

def main():
    data_karyawan = [
        Employee("Alice", 30, "E001"),
        Employee("Bob", 25, "E002"),
        Employee("Charlie", 40, "M001"),
        Employee("David", 28, "E004"),
        Manager("Charlie", 40, "M001", "IT", 4)

    ]
    # Print information about employees and manager
    for karyawan in data_karyawan:
        print(karyawan.get_info())

if __name__ == "__main__":
    main()