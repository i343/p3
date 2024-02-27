class Employee:
# Define the class attribute
    bonusPercent = 0.2
    
# Define and create the 'emp1' instance
emp1 = Employee()
emp1.firstName = "Maria"
emp1.lastName = "Rena"

# Define and create the 'emp2' instance
emp2 = Employee()
emp2.firstName = "Alex"
emp2.lastName = "Flora"

# Print class attribute
print(Employee.bonusPercent)

# Each instance is associated with the same class attribute value
print(emp1.firstName, emp1.lastName, emp1.bonusPercent)
print(emp2.firstName, emp2.lastName, emp2.bonusPercent)

# Accessing the class attribute by using the class name
Employee.bonusPercent = 0.3
print(Employee.bonusPercent)

# Accessing the class attribute by using the instance name
print(emp1.bonusPercent)
print(emp2.bonusPercent)

# Accessing the dictionary of the class and its objects
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)