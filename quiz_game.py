print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("OKAY! Let's play :)")

score = 0

answer = input("Whats does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Winner Winner :)")
    score +=1
    
else:
    print("Incorrect!")

answer = input("Whats does RAM stand for? ").lower()
if answer == "random access memory":
    print("Winner Winner :)")
    score +=1
else:
    print("Incorrect!")

print("You got " +str(score) + "questions correct!")
print("You got " +str((score / 2)*100) + "%.")