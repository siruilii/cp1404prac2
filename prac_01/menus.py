name=input("your name is")
menu="(H)ello "," (G)oodbye","(Q)uit"
print(menu)
choice=input(">>>").upper()
while choice != "Q":
   if choice == "H":
       print(f"hello {name}")
   elif choice == "G":
      print(f"goodbye {name}")
   else:
       print("invalid message")
   print(menu)
   choice=input(">>>").upper()
if choice=="Q":
    print("Finished")
