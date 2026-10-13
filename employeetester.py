class Employee:

    def __init__(self, **kwargs):
        self.name=kwargs["name"]
        self.identifier=kwargs["identifier"]
        self.salary=kwargs["salary", None]
    # Add your code here!

    def __str__(self):
        return self.name+","+self.identifier+","+self.salary
    # Add your code here!


chris = Employee(name="Chris", identifier="UT1")
print(chris, "\n")
