
import random
import string

n = int(input("Entrez la longueur de votre code : "))

characters = (
    string.ascii_letters
    + string.digits
    + string.punctuation
)

resulte = ""

for i in range(n):
    car = random.choice(characters)
    resulte += car

print(f"Your password is: {resulte}")
