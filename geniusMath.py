#Input get the answer from the user of the problem 4*4+4*4+4-4*4
#Procesing CALCULATE (4*4)+(4*4)+4-(4*4) and then diff=actual answer-user answer
# result=(diff % 3)*1.6 + 26
#Output Print Result


print ("Are you genius?")
x = input ("Reply yes or no\n")
if x == "yes":
    print ("Here is the problem 4*4+4*4+4-4*4 solve it ")
    user_answer= float(input ("So what is your answer you came out with?"))
    admin_answer= float((4*4)+(4*4)+4-(4*4))
    difference = user_answer - admin_answer
    result = str ((difference % 3) * 1.6 + 26)
    if difference > 0:
        print ("Your answer is positive")
        print ("Your score is " + str(result))
    else:
        print ("Your answer is negative")
        print ("Your score is " + str(result))


else:
    print ("Go and learn Maths")

