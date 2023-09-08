class Employee():
    def __init__(self, access_type: str, name: str, job_title: str, salary: int):
        self.access_type = str(access_type)
        self.name = str(name)
        self.job_title = str(job_title)
        self.salary = int(salary)
    
    def get_stats(self)-> list:
        return [self.access_type, self.name, self.job_title, self.salary]


if __name__ == "__main__":

    # Note: Typehints for the intended inputs:
    # Employee() # uncomment & mouse hover

    # Create an employee object the intended way:
    try:
        billy = Employee("Admin", "Billy", "SysAdmin", 95000)
        print(billy.get_stats())
    except Exception as err_msg:
        print(err_msg)

    # Breaking some logical aspect of the forced types:
    try:
        sarah = Employee(1,1,1,"One")
        print(sarah.get_stats())
    except Exception as err_msg:
        print(err_msg)
    
    # Problems:
    # 1. Forced types can raise unexpected exceptions.
    # Unspecific error handling required.
    # 2. We're not actually checking if the data makes sense.
    # We're simply just forcing it to fit the required type.