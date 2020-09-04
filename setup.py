import json
import os


usr = input("Pick a username\n")

if os.path.exists(f"profile_{usr}.json"):
  print("Username already exists! Please pick a different username.")
else:
  name = input("What's your name?\n")

  age = input("How old are you?\n")

  adr = input("What's your address?\n")

  by = input("What year were you born?\n")

  db = {
    "username": usr,
    "name": name,
    "age": age,
    "address": adr,
    "byear": by
  }
  # Hey look guys I'm doing a Nathan!
  with open(f"profile_{usr}.json", "w") as prf:
    json.dump(db, prf)