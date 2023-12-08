### Day 10 simulate rolling a pair of dice and tallying a specified number of times.
### Display actual results counts as well as the expected or theoretical percentage.
### Day 10 Python= Two dice Simulation 
### James Shoemaker 11/27/23


import random # for the add on randint() method call


def main():
    another = 'y'
    ExpectedProb = [0,0,1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]  # theoretical percentage roll 2 dice
    while (another == 'y'): 
        # prompt for specified number of rolls
        result2Dice = [0] * 13      # actual counts list initialized to zeros
        NumRoll = int(input("Enter number of rolls as an integer:  "))
        for x in range(NumRoll):
            result = random.randint(1,6) + random.randint(1,6)      # roll 2 and store result
            result2Dice[result] += 1                                # tally result to list
        print ('Num----Total Act Actual Pct               Expected Pct')  # heading on report
        for i in range(2,13,1):                                     # loop to print number of times 2-12 happened
            resultPct = result2Dice[i]/NumRoll
            print (f'{i:3} - {result2Dice[i]:7}    {resultPct:^7.2%}    \
                     {ExpectedProb[i]:^7.2%}')          # print results formatted
        another  = input("Another run?(y):  ")
# call main() module
main()