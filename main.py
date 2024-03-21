import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import rsa

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

running = True

# publicKey = (6910620973931493443928815804481544782831266029470470074737065723154751383177209404887088168084805959692528569912680980539089031200661215369814319296675603, 65537)
# privateKey = (6910620973931493443928815804481544782831266029470470074737065723154751383177209404887088168084805959692528569912680980539089031200661215369814319296675603, 65537, 5470649049369666163609425099597281304882263650685222972480182290660110415147397115950863677612301875318520696162097035273406790240973667233608460213760913, 4493009700412058253988303241001522620836427004461472455511049345217527431214622633, 1538082807454814470531759001940012319195265410291437370248873352162752091)
# with open('public.pem', mode='rb') as publicfile:
#    keydata = publicfile.read()
# publicKey = rsa.PublicKey.load_pkcs1(keydata)
# print(publicKey)

# with open('private.pem', mode='rb') as privatefile:
#    keydata = privatefile.read()
# privateKey = rsa.PrivateKey.load_pkcs1(keydata)


user = (input("What is your username: "))
user = user.upper()

while running:
   print("\nWhat would you like to do " + user + "?")
   print("1. Create a new entry")
   print("2. View entries")
   print("5. Exit")

   choice = int(input(">>"))

   if choice == 1:
      name = input("\nName: ")
      username = input("Username: ")
      password = input("Password: ")

      # encPassword = rsa.encrypt(password.encode(), publicKey)

      doc_ref = db.collection(user).document(name)
      doc_ref.set({"username": username, "password": password})

      print("Entry Added!\n")

   elif choice == 2:
      collection_ref = db.collection(user)
      entries = collection_ref.stream()

      print("\nEntries: ")
      for entry in entries:
         print(entry.id.capitalize())


   elif choice == 5:
      print("Goodbye!\n")
      running = False
   else: 
      print("Invalid Input!\n")

   






# doc_ref = db.collection("users").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

# doc_ref = db.collection("users").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
