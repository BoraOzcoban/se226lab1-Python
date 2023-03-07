name = input("What is your name?")
lab = int(input("Please enter your lab grade: "))
midterm = int(input("Please enter your midterm grade: "))
final = int(input("Please enter your final grade: "))
lastScore = (25*lab + 35*midterm + 40*final) / 100

print(f" Name: {name} \n Lab: {lab} \n Midterm: {midterm} \n Final: {final} \n Last Score: {lastScore} \n")