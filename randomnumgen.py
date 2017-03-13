#import the random module
import random
import time

#generate random number method
ranumber = random.randint(1, 20)

#program introduces itself
print("Hello, Im a random number generator.")
time.sleep(5) #add a time delay of 5 seconds
print("Right now, i am thinking of a number between 1 and 20. I bet you cant guess it")
time.sleep(5) #add another time delay of 5 seconds

#ask for user input
while 1==1:
   guess = int(input("Please guess a number: "))

   if guess < ranumber:
      print("Your guess was too low.")
   elif guess > ranumber:
       print("Your guess was too high.")
   else:
       print("You're right! Well done")
       break

