import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import rsa
import getpass

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

valid_user = False
running = True
EXCLUDE_ENTRY = "MASTER_ACCOUNT"

def listEntries():
   collection_ref = db.collection(master_user)
   entries = collection_ref.stream()

   # print("\nEntries: ")
   for entry in entries:
      if entry.id != EXCLUDE_ENTRY:
         print(entry.id)

# publicKey = (6910620973931493443928815804481544782831266029470470074737065723154751383177209404887088168084805959692528569912680980539089031200661215369814319296675603, 65537)
# privateKey = (6910620973931493443928815804481544782831266029470470074737065723154751383177209404887088168084805959692528569912680980539089031200661215369814319296675603, 65537, 5470649049369666163609425099597281304882263650685222972480182290660110415147397115950863677612301875318520696162097035273406790240973667233608460213760913, 4493009700412058253988303241001522620836427004461472455511049345217527431214622633, 1538082807454814470531759001940012319195265410291437370248873352162752091)
# with open('public.pem', mode='rb') as publicfile:
#    keydata = publicfile.read()
# publicKey = rsa.PublicKey.load_pkcs1(keydata)
# print(publicKey)

# with open('private.pem', mode='rb') as privatefile:
#    keydata = privatefile.read()
# privateKey = rsa.PrivateKey.load_pkcs1(keydata)

while valid_user == False:
   master_user = input("What is your username: ")
   master_user = master_user.upper()

   collection_ref = db.collection(master_user)
   entries = collection_ref.stream()
   if len(list(entries)) == 0:
      create_user = input("\nThat user does not exist. Would you like to create a new user? [y/n]")
      if create_user == "y":
         print("Please enter new user information: ")
         master_user = input("Username: ")
         master_user = master_user.upper()
         master_pass = input("Password: ")
         doc_ref = db.collection(master_user).document("MASTER_ACCOUNT")
         doc_ref.set({"MASTER_PASS": master_pass})
         print("User Created!\n")
      else:
         pass
   else:
      master_pass = getpass.getpass(prompt="Master Password: ")
      doc_ref = db.collection(master_user).document("MASTER_ACCOUNT")
      doc_snapshot = doc_ref.get()
      entry = doc_snapshot.to_dict()
      entry_pass = entry.get('MASTER_PASS')
      if master_pass == entry_pass:
         print(f"Welcome {master_user}\n")
         valid_user = True
      else:
         print("Incorrect Pasword!\n") 
      # print(entry_pass)

while running:
   print("\nWhat would you like to do " + master_user + "?")
   print("1. Create a new entry")
   print("2. View an entry")
   print("3. Delete an entry")
   print("4. Edit an entry")
   print("5. Exit")

   choice = int(input(">>"))

   if choice == 1:
      name = input("\nName: ")
      username = input("Username: ")
      password = input("Password: ")

      # encPassword = rsa.encrypt(password.encode(), publicKey)

      doc_ref = db.collection(master_user).document(name)
      doc_ref.set({"username": username, "password": password})

      print("Entry Added!\n")

   elif choice == 2:
      print("\nWhich entry would you like to view?")

      listEntries()

      view_entry = input(">>")
      doc_ref = db.collection(master_user).document(view_entry)
      doc_snapshot = doc_ref.get()
      entry = doc_snapshot.to_dict()
      entry_pass = entry.get("password")
      print(entry_pass)


   elif choice == 3:
      print("\nWhich entry would you like to delete?")

      listEntries()

      delete_entry = input(">>")
      delete_confirm = input(f"Are you sure you want to delete your entry for {delete_entry}? (THIS CANNOT BE UNDONE) [y/n]\n")
      if delete_confirm == 'y':
         db.collection(master_user).document(delete_entry).delete()
         print("\nEntry deleted!\n")

   elif choice == 4:
      print("Which entry would you like to edit?")
      listEntries()
      edit_entry = input(">>")
      edit_entry_name = input("Name: ")
      edit_entry_username = input("Username: ")
      edit_entry_password = input("Password: ")

      doc_ref = db.collection(master_user).document(name)
      doc_ref.set({"username": username, "password": password})

   elif choice == 5:
      print("Goodbye!\n")
      running = False
   else: 
      print("Invalid Input!\n")

   






# doc_ref = db.collection("users").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

# doc_ref = db.collection("users").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
