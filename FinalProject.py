points = 100
print("Welcome to Hunter Island! I am Leslie.")
import time
#sleep
print("")
time.sleep(2)
print("")
print("I am guessing that you came here to find the legendary Hunter's Treasure.")
import time
#sleep
print("")
time.sleep(3)
print("")
print("What is your name?")
import time
#sleep
print("")
time.sleep(1)
print("")
name = input("Name: ")
def greet(name):
    return "Hi, " + name
print (greet(name))
print("You begin to follow Leslie. As you follow him, the two of you get to a fork in the road. Do you want to go right to the jungle, or to the left into the caverns?")
Answer = input("Right or Left: ")
if Answer == ("Right"):
    print("Correct Answer. You will gain 10 points")
    print(points +10, "Points Left.")
else:
    print("Wrong Answer. You will lose 10 points, but also gain 5 points going to the jungle.")
    print("You scramble back to the forest.")
    print(points - 10 + 5, "Points Left.")
print("As you head into the jungle, Leslie tells you: ")
print("My good friend ", name, ", behind one of these objects is the legendary Hunter's Treasure.")
print("Here are the names: ")
names = ['The big Rock','Waterfall','Shed']
print(names[0])
print(names[1])
print(names[2])
print("Do you want to go to the big Rock, Waterfall, or the Shed first?")
answer2 = input("Answer: ")
if answer2 == ("the big Rock"):
    print("As you look all around the big rock, you find nothing but a mouse. This not where the treasure is but you can try again at shed or waterfall.")
    answer3 = input("Answer: ")
    if answer3 == ("Shed"):
        print("Correct. You have beat the game and found the treasure!!!!")
    else:
        print("Wrong answer again. Go find the treasure behind the shed.")
        print("You go to the shed and find the treasure. Yay. You have successfully beat the game and found the treasure!!!!")

if answer2 == ("Shed"):
    print("correct answer. You have completed the quest. ")
else:
    print("Wrong answer again. Go find the treasure behind the shed.")
    print("You go to the shed and find the treasure. Yay. You have successfully beat the game and found the treasure!!!!")

