from .Employee import Employee

class Manager(Employee):
    def __init__(self, name: str, age: int, employee_id: str, department: str,jumlah_karyawan: int):
        super().__init__(name, age, employee_id)
        self.department = department
        self.jumlah_karyawan = jumlah_karyawan

    def get_info(self) -> str:
        return f"Manager Name: {self.name}, Age: {self.get_age()}, Employee ID: {self.employee_id}, Department: {self.department}, Jumlah Karyawan: {self.jumlah_karyawan}"