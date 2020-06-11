#COSC.151.100
#Spring 2020
#James E. Fitzgerald III
#Final Exam




print("Welcome to the Number Generator!")




import random   #   This function will import to generate a random number
def number_generator(): # This definition functionn will identify the random number generator
    random_number=random.randint(100, 1000) # declares the variable to store generated number
    return random_number # this will return the value of the variable that is added to the number generator

number_generator()

def user_number(): # This definition will identify the main funtion
   user_number =int (input("Please enter any whole number:  ")) # This variable will ask the user to enter any whole number.    
   write_file= open("numbergenerator.txt", "w") # Will create a text file in write mode named numbergenerator.txt 
   for random_numbercount in range(1, user_number +1 ): # This for loop will identify the users input; and run random numbers for the number of times entered
      random_number=number_generator() # Will store the numbers generated inside random_number viarable
      write_file.write(str(random_number)+ "\n")# Will write each random number in the random_number viarable on a new line in the text file numbergenerator.txt
      
user_number()
