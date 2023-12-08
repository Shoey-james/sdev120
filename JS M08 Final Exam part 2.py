# James Shoemaker 12/1/23
# input a list of employee names and salaraies and store them in parallel arrays, end the input with a sentinel value
# find the average salary of employees, then find the names of any employee who's salary is within 5000 of the average salary
# all salaries should be displayed to the nearest 100 and entered as floating point numbers (ex. 36,525 --> 36.5)

def getAverageSalary(salary):       # function to determine average salary
    totalSalary, count = 0, 0
    for sal in salary:              # iterate over list salary
        totalSalary += sal          # add salary to total salary, assign resultant value to a variable 
        count += 1                  # increment
    avgSal = totalSalary/count      # get average salary
    return avgSal                   # send function result back to caller



def main():
    print("Enter employee salary as follows --> 36,525 would be 36.5")  # example for user to understand how to input the employee salary in next line
    name, salary, = [], []          # create lists for name and salary
    emp_name = input("Enter employee's name or n to finish: ")              # prompt for employee name with sentinel value to end input
    while emp_name != "n":                                                  # loop runs until "!" is entered to signify end of input for employee names
        name.append(emp_name)
        emp_salary = float(input("Enter employee salary for " + emp_name+ ": "))    # floating employee salary from prompted user imput pertaining to specific employee name
        salary.append(emp_salary)
        emp_name = input("Enter employee name or put n to finish: ");
    if len(salary) == 0:
        return
    average_salary = getAverageSalary(salary)       # call to function getAverageSalary
    less_than_average_salary = average_salary - 5   # determine 5000 less than average salary
    higher_than_average_salary = average_salary + 5 # determine 5000 more than average salary
    print()
    print("Employees within 5000 of the average are: ")
    for i in range(len(salary)):                    # iterate over list salary
        if salary[i] >= less_than_average_salary and salary[i] <= higher_than_average_salary:
            print(name[i],",", format(salary[i]*1000, ".2f"))       # print the name and salary, format float value
    print("The average employee salary is: ", format(getAverageSalary(salary)*1000, ".2f")) # formatting and printing average employee salary
    print(name, salary) # displays contents of name and salary lists
     
main()          # call function main

