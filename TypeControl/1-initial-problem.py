class Employee():
    def __init__(self, access_type, name, job_title, salary):
        self.access_type = access_type
        self.name = name
        self.job_title = job_title
        self.salary = salary
    
    def get_stats(self)-> list:
        return [self.access_type, self.name, self.job_title, self.salary]


if __name__ == "__main__":

    # Note: No specificiation for intended variable types:
    # Employee() # uncomment & mouse hover

    # Expected way create an employee:
    billy = Employee("Admin", "Billy", "SysAdmin", 95000)
    print(billy.get_stats())

    # Create an employee object out of the intended context:
    sarah = Employee(1,1,1,1)
    print(sarah.get_stats())

    # Problems
    # 1. Variables can be passed as literally any object type.
    # Meaning, variables really don't mean anything at all.
    # 2. Note: No specificiation for intended variable types:
    # Employee() # uncomment & mouse hover