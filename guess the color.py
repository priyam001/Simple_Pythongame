import random
print("Color chice game:")
print("Select any number to choose a color:")
print("Press esc buttion to exit game.")
cs=0
ps=0
while True:
  print("1=red\n2=yello\n3=green\n4=blue\n5=black")
  pc=int(input("Enter number to select color:"))
  if pc > 5 :
    print("Invalid selection By user")
  else:
    cc=random.randint(1,5)
    print("Computer selcted",cc)

    if pc==cc:
      print("Both selceted same color , Match Draw!")
    if pc>cc:
      print("Player won")
      ps=ps+1
      print("Computer score",cs)
      print("Player Score:",ps)
    if pc<cc:
      print("Computer won")
      cs+=1
      print("Computer score",cs)
      print("Player Score:",ps)
