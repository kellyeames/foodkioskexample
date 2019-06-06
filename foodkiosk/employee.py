class Employee():
    def __init__(self, employeename, employeeemail):
        self.employeename=employeename
        self.employeeemail=employeeemail
    
    def getEmployeeName(self):
        return self.getEmployeeName

    def getEmployeeEmail(self):
        return self.employeeemail

    def __str__(self):
        return self.employeename + ", " + self.employeeemail