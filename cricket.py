import random
sum=0
for i in range(1,8):
 if i==7:
        print("Over")
 else:
  print("Computer turn: (1) (2) (3) (4) (5)")
  randscore=random.randint(1,5)
  comp=randscore
  you=int(input("Your turn: (1) (2) (3) (4) (5) "))
  print("Computer chooses",comp)
  print("You chooses",you)
  if comp==you:
            sum=0
            print("Out")
  elif comp!=you:
            sum = sum + comp
            print(f"your score is :",sum)
print("     Thank you for playing       ")
