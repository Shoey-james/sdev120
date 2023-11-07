# Day 5 Simulation with Python: Roll a pair of six sided dice
# James Shoemaker SDEV120 11/6/2023
# Generate random number between or equal to 1-6 for each die
# will have a while loop. Do pay attention to indenting.

def main():
    another='y'                                                             # sentinal value for loop default to run 1 time
    while (another == 'y'):
                                                                            # do roll a specified number of times
        numRoll = int(input("Enter number of rolls as an integer: "))
        import random                                                       # built in random number generator
        seedno = int(input("Enter integer seed number (0 to not declare): "))
        if (seedno > 0):
            random.seed(seedno)                                             # predictable if you know your seed number
        for x in range (numRoll):                                           # determined loop know number of iterations
            result = random.randint(1,6) + random.randint(1,6)              # 2 dice simulation 1-6 for each
        #   res1 = random.randint (1,6)                                     # displaying dice counts separately in output
        #   res2 = random.randint (1,6)                                     # displaying dice counts separately in output
        #   result = res1 + res2                                            # result displaying dice counts separately
            print(result)
        #   print(res1, " + ", res2, " = ",result)                          # printed result displaying dice counts separately
        another = input("Another run? (y): ")
    print(" ** End Program **")
main ()                                                                     # execture main() module/method

