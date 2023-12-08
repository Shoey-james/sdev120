# James Shoemaker 12/5/23
# Day 12 File Input and Output 
# Write a program that writes a series of random numbers.  Number Range 1 to 500 integers.  Get user prompt for the total number to generate and write.
# For the above created file read in and display all the numbers.  Accumulate the total number as well as the sum of numbers.  Display these as well as the average at the end.



def main():
    import random       # import access to pseudorandom number generator
    numRolls = int(input("Enter number of random numbers desired: "))
    outFile = open("desktop/Computing Logic/Python/numbers.txt",'a') # open output file, have to direct where to save the file to be written
    for i in range (numRolls):
        randomNum = random.randint(1,500)   # generate the number
        outFile.write(str(randomNum)+'\n')  # output to the file
    outFile.close()     # write buffer contents and close file
    print("End program")
main()      # exectute main () module