
gryffindor=0
ravenclaw=0
hufflepuff=0
slytherin=0
q1=int(input("do you like dawn or dusk? \n1.dawn \n2.dusk \n Enter answer (1-2):"))
if q1==1:
  gryffindor+=1
  ravenclaw+=1
elif q1==2:
  hufflepuff+=1
  slytherin+=1
else:
  print("wrong input")

q2=int(input("when i'm dead, i wnat people to remember me as:\n1.the good \n2.the great \n3.the wise \n4.the bold \n Enter your anwser(1-4):"))
if q2==1:
  hufflepuff+=2
elif q2==2:
  slytherin+=2
elif q2==3:
  ravenclaw+=2
elif q2==4:
  gryffindor+=2
else:
  print("wrong input.")

q3=int(input("which kind of instrument most pleases your ear? \n1.the violin \n2.the trumpet \n3.the piano \n4.the drum \nEnter the your answer (1-4):"))
if q3==1:
  slytherin+=4
elif q3==2:
  hufflepuff+=4
elif q3==3:
  ravenclaw+=4
elif q3==4:
  gryffindor+=4
else:
  print("wrong input.")

if hufflepuff>ravenclaw:
  print("huffflepuff have the most points:",hufflepuff)
elif ravenclaw>gryffindor:
  print("ravenclaw have the most points:",ravenclaw)
elif gryffindor>slytherin:
  print("gryffindor have the most points:",gryffindor)
else:
  print("slytherin have the most points:",slytherin)