"""
Author: Idan Chernetsky
The program arranges numbers in an ascending order.
"""

counter0s = 0
# insert first digit and checks for illegal inputs
newDigit = input("Insert a number between 1-9:")
while (newDigit.isdigit() == False) or (int(newDigit) < 0 or int(newDigit) > 9):
    if newDigit == 0:
        counter0s = counter0s + 1
        continue
    print ("'", newDigit, "' is not between 1-9, please try again.")
    newDigit = input("Insert a number between 1-9:")

newDigit = int(newDigit);

# insert second digit and checks for illegal inputs
num = input("Insert a number between 1-9:")
while (num.isdigit() == False) or (int(num) < 0 or int(num) > 9):
    if num == 0:
        counter0s = counter0s + 1
        continue
    print ("'", num, "' is not between 1-9, please try again.")
    num = input("Insert a number between 1-9:")
num = int(num)

# sorts first two digits
if newDigit >= num:
    num = (num * 10) + newDigit
else:
    num = (newDigit * 10) + num

# counts every new digit
counter = 2
# main loop for sorting the digits
while counter != 7:
    # insert new digit and checks for illegal input
    newDigit = input("Insert a number between 1-9:")
    while (newDigit.isdigit() == False) or (int(newDigit) < 0 or int(newDigit) > 9):
        if newDigit == 0:
            counter0s = counter0s + 1
            continue
        print ("'", newDigit, "' is not between 1-9, please try again.")
        newDigit = input("Insert a number between 1-9:")
    newDigit = int(newDigit)
    # increment the digit counter
    counter = counter + 1
    # checks if last digit is bigger than the full number's last digit and concatenates it
    if newDigit >= num % 10:
        num = (num * 10) + newDigit
    else:
        # checks if last digit is smaller than the full number's last digit and arranges it
        temp = num
        # collects the digits which are bigger than the new one
        temp2 = 0
        # counts the place for the new digit
        counter10s = 0
        # goes through all the digits inserted until now
        for i in range(counter):
            # pushes the new digit in place and breaks the loop
            if newDigit >= temp % 10:
                temp = (temp * 10) + newDigit
                num = (temp * (10**counter10s)) + temp2
                break
            # calculates intermediate results
            temp2 = temp2 +((temp % 10) * (10** counter10s))
            temp = int(temp / 10)
            counter10s = counter10s + 1
# prints the result :)
print("The new number is: ", str(num).zfill(7))
    
