# Define the class
class Employee: 
    pass

# Create two instances/objects based on the class
emp1 = Employee()
emp2 = Employee()

# Provide attributes and assign values to the instances
emp1.firstName = "Maria"
emp1.lastName = "Rena"
emp1.basicSalary = 12000
emp1.allowance = 5000
emp2.firstName = "Alex"
emp2.lastName = "Flora"
emp2.basicSalary = 15000
emp2.allowance = 5000

# Print the objects and their attributes
print(emp1.firstName, emp1.lastName)
print(emp2.firstName, emp2.lastName)