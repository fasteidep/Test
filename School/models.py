from dataclasses import dataclass
from enum import Enum
class Chel:
    def __init__(
        self,
        name:str,
        last_name:str,
        age:int,
        ) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age

class StudSubj(Enum):
    MATH = 'math'
    GEOGRAPHY = 'geography'
    PE = 'pe'

class Student:
    def __init__(
        self,
        grades:dict[StudSubj, float]
        ) -> None:
        self.grades = grades

@dataclass
class StudClass:
    name:str
    stud_list:list[Student]

        
class Teacher(Chel):
    def __init__(self, name: str, last_name: str, age: int, class_:int, ) -> None:
        super().__init__(name, last_name, age)
