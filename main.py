import json
from datetime import datetime

with open("tips.json", "r") as file:
    data = json.load(file)

name = input("Enter your name: ")
print("Hello,", name)

while True:
    print("\n1. Study Tip")
    print("2. Motivation Quote")
    print("3. Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = data["study_tips"][0]
        print(result)

    elif choice == "2":
        result = data["quotes"][0]
        print(result)

    elif choice == "3":
        result = str(datetime.now())
        print(result)

    elif choice == "4":
        print("Thank You")
        break

    else:
        result = "Invalid Choice"
        print(result)

    with open("output.txt", "a") as f:
        f.write(result + "\n")