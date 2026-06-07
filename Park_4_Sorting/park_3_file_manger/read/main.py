open_file = open("../create/data_kariwan.txt", "r")
data_karyawan = []
for line in open_file:
    data = line.strip().split(",")
    if len(data) == 3:
        name, age, employee_id = data
        data_karyawan.append({"name": name, "age": int(age), "employee_id": employee_id})
    elif len(data) == 5:
        name, age, employee_id, department, jumlah_karyawan = data
        data_karyawan.append({"name": name, "age": int(age), "employee_id": employee_id, "department": department, "jumlah_karyawan": int(jumlah_karyawan)})
open_file.close()

for karyawan in data_karyawan:
    if "department" in karyawan:
        print(f"Manager Name: {karyawan['name']}, Age: {karyawan['age']}, Employee ID: {karyawan['employee_id']}, Department: {karyawan['department']}, Jumlah Karyawan: {karyawan['jumlah_karyawan']}")
    else:
        print(f"Employee Name: {karyawan['name']}, Age: {karyawan['age']}, Employee ID: {karyawan['employee_id']}")