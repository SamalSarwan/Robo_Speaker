import os

print("Welcome to Robo Speaker...[exit-to exit the app]")
while True:
    x=input("Enter what you want to say: ")
    if(x=="exit"):
        os.system("say 'Exiting from the program'")
        break
    os.system(f"say {x}")