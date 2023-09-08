from enum import Enum

class AccessLevel(Enum):
    ADMIN = 1
    CLIENT = 2
    USER = 3

class JobTitle(Enum):
    CEO = 1
    CTO = 2
    CFO = 3
    SYSADMIN = 4
    DBADMIN = 5
    DEVELOPER = 6

class Employee():
    def __init__(self, access_level: AccessLevel, name: str, job_title: JobTitle, salary: int):

        self.validate_type(var_name="access_level", var_value=access_level, var_type=AccessLevel)
        self.validate_type(var_name="name", var_value=name, var_type=str)
        self.validate_type(var_name="job_title", var_value=job_title, var_type=JobTitle)
        self.validate_type(var_name="salary", var_value=salary, var_type=int)

        self.access_type = access_level
        self.name = name
        self.job_title = job_title
        self.salary = salary
    
    def validate_type(self, var_name, var_value, var_type)-> None:
        if not isinstance(var_value, var_type):
            raise TypeError(f"TypeError: Employee.{var_name}:{var_value} is of {type(var_value)} but must be of {var_type}.")

    def get_stats(self)-> list:
        return [self.access_type, self.name, self.job_title, self.salary]

if __name__ == "__main__":
    
    # Valid Attempt
    try:
        billy = Employee(AccessLevel.USER, "Billy", JobTitle.SYSADMIN, 95000)
        print(billy.get_stats())

    except TypeError as err_msg:
        print(err_msg)

    # Unique type controlled pre-defined variables
    try:
        sarah = Employee("Admin","Billy","SysAdmin",95000)
        print(sarah.get_stats())
    except TypeError as err_msg:
        print(err_msg)