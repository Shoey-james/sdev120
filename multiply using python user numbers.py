"""
Day 2b- Input two numbers, Multiply them and display (print) results
        James Shoemaker - 10/25/2023

"""

num_1 = float(input("Enter the first number: ")) # input first number AND turned into a floating point all together
num_2 = float(input("Enter the second number: ")) # input second number AND turned into a floating point all together
product = num_1 * num_2  #process. Multiply and store result
print("Product of {} and {} is {}".format(num_1, num_2,product)) #echoes the input values as well as puts them in the curly brackets to be more user friendly. Uses f string where the {} will be replaced by the input numbers
        
