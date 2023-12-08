# James Shoemaker 12/1/23              Final Project - Programming
# Input trainer names and enrollees
# output number trainers who have enrolled members in 3 categories - (0-5),(6-10),(11-15) new members
# write program to input 15 trainer names and number new  members they have enrolled into an array
# Output is to display the number of trainers who are in each category




def main():
    trainerName =[]       # create Empty list for trainer name
    trainerNoMembers = []  # create empty parallel list for number members
    trainer_file = open('./Desktop/Computing Logic/Python/trainerM-1.txt','r') # open existing file to read
    trainer_rec = trainer_file.readline()   # read first field up to newline
    num_emps = 0            # defining number of employees
    category1Count = 0      # defining category for trainers with (0-5) new members
    category2Count = 0      # defining category for trainers with (6-10) new members
    category3Count = 0      # defining category for trainers with (11-15) new members
    losingMembers = 0     # account for negative members, loss of member from trainer
    category4Count = 0      # accont for a trainer gaining more than >15 new members


    while (trainer_rec != ''):   # != means not equal
        trainerName.append(trainer_file.readline().strip())  # append to lists
        trainerNoMembers.append(int(trainer_file.readline()))
        num_emps+=1      # increment number of employees. += assigns two values together, assigns final value to variable
        trainer_rec = trainer_file.readline()   # read first field of next record
    for i in range(len(trainerNoMembers)):   # print contents of lists
        print("%2d%10s%5d" % \
              (i,trainerName[i],trainerNoMembers[i])) # configuring how table will be displayed in output
    for trainerNoMembers in trainerNoMembers:         # calling the number of trainer new members in a for statement - selections  
        if 0 <= trainerNoMembers <= 5:                # selection for those that fall into category 1
            category1Count += 1                       # increment for category1Count to display number of trainers in (0-5) category
        elif 6 <= trainerNoMembers <= 10:             # selection for those not in category 1
            category2Count += 1                       # increment for category2Count to display number of trainers in (6-10) category
        elif 11 <= trainerNoMembers <=15:             # selection for those not in category 2
            category3Count += 1                       # increment for category3Count to display number of trainers in (11-15) category
        elif 0 > trainerNoMembers:
            losingMembers += 1
        elif 15 < trainerNoMembers:
            category4Count += 1


    trainer_file.close()                              # courtesy close of trainer_file

    print('Trainers with (0-5) new members:', category1Count)          # display number of trainers in category 1 
    print('Trainers with (6-10) new members:', category2Count)         # display number of trainers in category 2 
    print('Trainers with (11-15) new members:', category3Count)        # display number of trainers in category 3
    print('Trainers with (>15) new members:', category4Count)          # display number of trainers with over 15 new members
    print('Trainers that have lost member(s):', losingMembers)          # display number of trainers with negative members added (loss of members)
    print('Total number employees:',num_emps)                          # echo number of employees in trainer_file
    print('Total number employee names in list:',len(trainerName))     # echo number of employee names in trainer_file

main()   # execute main module


