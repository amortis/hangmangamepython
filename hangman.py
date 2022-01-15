from wordlist import word_list
import random
def check1(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
def check(n):
    if check1(n) == True:
        n = int(n)
        if n>=0 and n<=5:
            return True
        else:
            return "Please choice the correct number"
    else:
        while check1(n) != True:
            return "Please type the integer"
def checklet(n):
    if len(str(n))>1 or check1(n)==True:
        return False
    else:
        return True
print("Welcome to the hangman game!!! You will have to guess the word by it's letters. For every wrong letter you will lose a live.")
print("Select the difficulty : ")
print("1. Easy - 15 lives")
print("2. Medium - 10 lives")
print("3. Hard - 5 lives")
print("4. Hardcore - 3 lives")
print("5. Choise your number of lives")
user1 = input()
while check(user1)!= True:
    print(check(user1))
    user1 = input("Try to type again ")
user = int(user1)
lives = 0
if user == 1:
    lives = 15
elif user == 2:
    lives = 10
elif user == 3:
    lives == 5
elif user == 4:
    lives == 3
elif user == 5:
    lives = input("Type your number of lives : ")
    while check1(lives)== False or int(lives)<=0:
        lives = input("Please try to type the correct numerical value")
print("Awesome! Let's start!\n")
lives = int(lives)
liveslost = 0

word = random.choice(word_list)
lenn = len(word)
wordprint = "_"*lenn
lets = []
while wordprint!=word and lives != 0:
    print("Your word right now : ", wordprint)
    print("Your already choisen letters : ", lets)
    print("Your current number of lives : ", lives)
    let = input("Type your letter : ").lower()
    print("\n")
    while checklet(let)==False:
        let = input("Type only 1 letter. ")
    if let in word:
        print("You're guessed. Keep going!\n")
        wordprint = ''
        for i in range(len(word)):
            if let == word[i]:
                wordprint+=word[i]
            else:
                wordprint+='_'
    else:
        print("There's no such letter in that word. :( Try again. You lost one your live.\n")
        lives-=1
        liveslost+=1
        lets.append(let)
if wordprint==word:
    print("Congratulations! You've guessed the word. It was : ", wordprint)
    print(f"You've lost {liveslost} lives!")
if lives==0:
    print("Sorry you've lost all your lives. Don't get upset and try again :). The correct word was : ", word)
    print(f"You've lost {liveslost} lives!")