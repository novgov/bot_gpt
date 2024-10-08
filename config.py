import shelve

db = shelve.open("pandora")
for key in db:
    print(f"{key} {db[key]}")
db.close()