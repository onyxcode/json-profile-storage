import os
import json


search = input("Please pick a username.\n")

if os.path.exists(f"profile_{search}.json"):
    with open(f"profile_{search}.json", "r") as prf:
        jD = json.load(prf)

        print(f'Username: {jD["username"]}\nName: {jD["name"]}\nAge: {jD["age"]}\nBorn in: {jD["byear"]}\nAddress: {jD["address"]}')
else:
    print("Username is available.")