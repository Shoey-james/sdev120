# James Shoemaker 12/6/23
# Hands on Day 12 program 2 Read
# Read in number.txt file created in program 1. accumulate total number of random numbers as well as accumulated sum. When complete, calculate and display the average.

def main():
    counter = 0        # track total number input           counter
    total = 0          # total of all the random numbers    accumulator
    inFile = open("desktop/Computing Logic/Python/numbers.txt",'r')     # open input file (read mode), have to direct where to find the file
    currNumberStr = inFile.readline()   # priming (first) read
    while (currNumberStr != ""):        # test for end of file  (EOF)
        currNumber = int(currNumberStr) # convert string to number
        counter += 1                    # counter = counter +1
        total += currNumber             # 
        print("Current number = ", currNumber)  # diagnostic print
        currNumberStr = inFile.readline()       # reading the next number
    avg = total/counter 
    print("Total of the numbers is: ", total)
    print("Average of ", counter ,"numbers is ", avg)
    inFile.close()                      # close input file
    print("End Program")
main() # execute main() module


