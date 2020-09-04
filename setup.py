import json
import os
import random


rnu = random.randrange(1)

usrn = input("Pick a username")

db = {
  "username":usr,
  "name":name,
  "age":age,
  "address":adr,
  "byear":by 
}
# Hey look guys I'm doing a Nathan!
if os.path.exists(f"profile_{usrn}.json"):
  print("Username already exists! Please pick a different username.")
else:
  with open(f"profile_{usrn}.json", "w") as prf:
    json.dump(db, prf)
    