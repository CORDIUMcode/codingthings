print("Hello, my name is CORDIUM")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Aw ok. Bye!")
    quit


score = 0

print ("Ok lets play!")

q1 = input("What does CPU stand for? ")
if q1.lower() == "central processing unit":
    print("Correct!")
    score += 1 
else:
    print("Incorrect.")

q2 = input("What does RAM stand for? ")
if q2.lower() == "random access memory":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

q3 = input("What does PSU stand for? ")
if q3.lower() == "power supply unit":
    print("Correct!")
    score += 1 
else:
    print("Incorrect.")

print("You got " + str(score) + " questions correct!")

print("You got a " + str((score / 3) * 100) + "%")

if score == 0:
    print("You suck!")
else: 
    print("Good job!")