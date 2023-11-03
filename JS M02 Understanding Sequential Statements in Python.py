salary = float(input("Input Salary: "))
numDependents = (input("Input dependents: "))

# Calculate stateTax here.
stateTax = (float(salary) * .065)
print("State Tax: $" + str(stateTax))

# Calculate federalTax here.
federalTax = (float(salary) * .28)
print("Federal Tax: $" + str(federalTax))

# Calculate dependantDeduction here.
dependentDeduction = (float(salary) * ((.025) * (float(numDependents))))
print("Dependents: $" + str(dependentDeduction))

# Calculate totalWithholding here.
totalWithholding = (stateTax + federalTax + dependentDeduction)
# Calculate takeHomePay here.
takeHomePay = ((float(salary)) - (float(totalWithholding)))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))