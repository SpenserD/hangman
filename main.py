import random
import time

name = input("Who is you? ")

print ("Sup, " + name, "Wanna play a game?")

time.sleep(1)

print ("Hurry Up...")

time.sleep(0.5)

wordbank = ["Steak", "Chicken", "Donuts", "Banana", "Breadsticks", "Orange", "Cake", "Honeydew", "Doritos", "Salad", "Jambalaya", "Pudding", "Jello", "Ham", "Lasagna", "Turkey", "Popcorn", "Biscuits", "Gravy", "Tempura", "Stuffing", "Potatoes", "Porkchop", "BBQ", "Cheese", "Sushi", "Croissant", "Paprika", "Pepper", "Tequila", "Macaroni", "Burrito", "Wings", "Cranberry", "Cantalope", "Sausage", "Pancakes", "Bagel", "Fries", "Shrimp"]
word = random.choice(wordbank)
guesses = ''
turns = 10
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print (char,end=""),   
        else:
            print ("_",end=""),     
            failed += 1   
    
    if failed == 0:        
        print (" was the word. You were just born better")
        break            
    guess = input(" gimme a letter:")
    guesses += guess                    
    
    if guess not in word:  
        turns -= 1        
        print ("Wrong")  
        print ("You have", + turns, 'more guesses' )
        if turns == 0:          
            print ("You suck LOSER!!!!"  )
