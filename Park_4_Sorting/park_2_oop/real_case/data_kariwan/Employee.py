from .Person import Person

class Employee(Person):
    def __init__(self, name: str, age: int, employee_id: str):
        super().__init__(name, age)
        self.employee_id = employee_id

    def get_info(self) -> str:
        return f"Employee Name: {self.name}, Age: {self.get_age()}, Employee ID: {self.employee_id}"