import random
game = ["Rock", "Paper", "Scissors"]
angka = random.randint(0,3)
answer = game[angka]
print("Kuy Mabar!")
guess = ""

while True:
    guess = input("Rock, Paper, Scissors :")
    if guess== "Rock" and answer== "Scissors":
        print ("Batu menang dari gunting")
    elif guess  == "Paper" and answer== "Rock":
        print ("Kertas menang dari batu")
    elif guess == "Scissors" and answer == "Paper"  :
        print ("Gunting menang dari kertas")
    elif guess == "Scissors" and answer == "Rock" :
        print ("Gunting kalah dari batu")
    elif guess == "Rock" and answer == "Paper" :
        print ("Batu kalah dari kertas")
    elif guess == "Paper" and answer== "Scissors" :
        print ("Kertas kalah dari gunting")
    elif guess == "Paper" and answer == "Paper" :
        print ("seri")
    elif guess == "Rock" and answer == "Rock" :
        print ("seri")
    else:
        print ("Seri")