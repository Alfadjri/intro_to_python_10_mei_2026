from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    @abstractmethod
    def get_info(self) -> str:
        pass

    def get_age(self):
        return self.__age
        
    def set_age(self, age: int):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.__age = age